#!/usr/bin/env python3
"""Exercise product installation and source migration in disposable repositories."""

import hashlib
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile


def run(cwd, *args, ok=True):
    result = subprocess.run(args, cwd=cwd, env=ENV, capture_output=True)
    if ok and result.returncode:
        raise AssertionError(result.stderr.decode())
    return result


def git(cwd, *args):
    return run(cwd, 'git', *args).stdout.decode().strip()


def identity(path):
    git(path, 'config', 'user.name', 'Separation fixture')
    git(path, 'config', 'user.email', 'fixture@example.invalid')


def snapshot(repo, revision, destination):
    destination.mkdir(parents=True)
    names = run(repo, 'git', 'ls-tree', '-rz', '--name-only', revision).stdout
    for raw in names.split(b'\0'):
        if not raw:
            continue
        name = raw.decode()
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(run(repo, 'git', 'show', revision + ':' + name).stdout)


def files(path):
    return {
        p.relative_to(path).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in path.rglob('*')
        if p.is_file() and '.git' not in p.relative_to(path).parts
    }


def lean(path):
    names = files(path)
    for required in ['LICENSE', 'RAILSPIKE.md', 'WELCOME.md',
                     'docs/workflow/step1_solution_assessment.md']:
        assert required in names, required
    assert not any(p.startswith(('docs/plans/', 'docs/maintainers/',
                                 'docs/research/', 'scripts/')) for p in names)
    assert not any(p in names for p in ['index.html', 'railspike-logo.png', '.nojekyll'])
    return names


ENV = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_CONFIG_GLOBAL='/dev/null',
           GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_COUNT='1',
           GIT_CONFIG_KEY_0='protocol.file.allow', GIT_CONFIG_VALUE_0='always')


def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: check-repository-separation.py PRODUCT_SOURCE LEGACY_REVISION')
    source, legacy_revision = sys.argv[1:]
    with tempfile.TemporaryDirectory(prefix='railspike separation ') as directory:
        root = Path(directory)
        product = root / 'product'
        git(root, 'clone', '-q', source, str(product))
        current = git(product, 'rev-parse', 'HEAD')
        git(product, 'merge-base', '--is-ancestor', legacy_revision, current)
        expected = lean(product)

        # A complete snapshot copy preserves unrelated dirty/staged host work.
        host = root / 'copy-host'
        host.mkdir()
        git(host, 'init', '-q', '--initial-branch=main')
        identity(host)
        (host / 'work.txt').write_text('committed\n')
        git(host, 'add', '.')
        git(host, 'commit', '-qm', 'host')
        (host / 'work.txt').write_text('staged\n')
        git(host, 'add', 'work.txt')
        (host / 'work.txt').write_text('unstaged\n')
        index_before = git(host, 'ls-files', '-s')
        installed = host / 'docs/railspike'
        snapshot(product, current, installed)
        assert lean(installed) == expected
        record = '# Source\nRepository: ' + source + '\nRevision: ' + current + '\n'
        (installed / 'RAILSPIKE_SOURCE.md').write_text(record)
        assert git(host, 'ls-files', '-s') == index_before
        assert (host / 'work.txt').read_text() == 'unstaged\n'
        plans = host / 'docs/plans'
        plans.mkdir()
        (plans / 'fixture_step1_solution_assessment.md').write_text(
            '## Original Query\nCompare export formats.\n')
        assert not (installed / 'docs/plans').exists()

        # Exercise the documented copy-migration reconciliation and rollback.
        baseline = root / 'legacy-baseline'
        snapshot(product, legacy_revision, baseline)
        assert (baseline / 'docs/plans').is_dir()
        old = root / 'old-copy'
        shutil.copytree(baseline, old)
        local_note = '\nLocal installation note.\n'
        with (old / 'README.md').open('a') as handle:
            handle.write(local_note)
        local_plan = old / 'docs/plans/local-only.md'
        local_plan.write_text('Locally authored plan; preserve me.\n')
        (old / 'RAILSPIKE_SOURCE.md').write_text('Legacy revision: ' + legacy_revision + '\n')
        before = files(old)
        recovery = root / 'recovery-copy'
        shutil.copytree(old, recovery)
        prepared = root / 'prepared'
        snapshot(product, current, prepared)
        with (prepared / 'README.md').open('a') as handle:
            handle.write(local_note)
        (prepared / 'RAILSPIKE_SOURCE.md').write_text(record + 'Retained local README note.\n')
        preserved_plan = plans / 'recovered-local-only.md'
        shutil.copy2(local_plan, preserved_plan)
        assert preserved_plan.read_bytes() == local_plan.read_bytes()
        assert not (prepared / 'docs/plans').exists()
        assert (prepared / 'README.md').read_text().endswith(local_note)
        assert files(recovery) == before
        # Simulate a failed verification before accepting the replacement.
        failed = root / 'failed-copy'
        shutil.copytree(prepared, failed)
        (failed / 'LICENSE').unlink()
        try:
            lean(failed)
        except AssertionError:
            restored = root / 'restored-copy'
            shutil.copytree(recovery, restored)
            assert files(restored) == before
        else:
            raise AssertionError('Incomplete replacement was not detected')

        # Actual old and new Git histories, not dummy workflow files.
        old_remote, new_remote = root / 'old.git', root / 'new.git'
        git(root, 'clone', '-q', '--bare', str(product), str(old_remote))
        git(old_remote, 'update-ref', 'refs/heads/master', legacy_revision)
        git(old_remote, 'symbolic-ref', 'HEAD', 'refs/heads/master')
        git(root, 'clone', '-q', '--bare', str(product), str(new_remote))
        subhost = root / 'submodule-host'
        subhost.mkdir()
        git(subhost, 'init', '-q', '--initial-branch=main')
        identity(subhost)
        git(subhost, 'submodule', 'add', str(old_remote), 'docs/railspike')
        git(subhost, 'config', '-f', '.gitmodules', 'submodule.docs/railspike.branch', 'master')
        git(subhost, 'config', 'submodule.docs/railspike.branch', 'master')
        git(subhost, 'add', '.gitmodules', 'docs/railspike')
        git(subhost, 'commit', '-qm', 'legacy installation')
        sub = subhost / 'docs/railspike'
        modules_before = (subhost / '.gitmodules').read_bytes()
        revision_before = git(sub, 'rev-parse', 'HEAD')
        block = (product / 'README.md').read_text().split('<!-- railspike-update-start -->')[1]
        block = block.split('<!-- railspike-update-end -->')[0]
        block = '\n'.join(line for line in block.splitlines() if not line.startswith('```'))
        block = block.replace('https://github.com/rlspk/railspike.git', shlex.quote(str(new_remote)))
        command = root / 'update.sh'
        command.write_text(block)
        rejected = run(subhost, 'bash', str(command), ok=False)
        assert rejected.returncode != 0 and b'Unexpected registered URL.' in rejected.stderr
        assert git(subhost, 'status', '--porcelain') == ''
        assert git(sub, 'rev-parse', 'HEAD') == revision_before
        # Deliberate source migration: review/fetch before changing any URL.
        def migrate():
            git(sub, 'fetch', str(new_remote), 'main')
            reviewed = git(sub, 'rev-parse', 'FETCH_HEAD')
            git(sub, 'merge-base', '--is-ancestor', revision_before, reviewed)
            git(subhost, 'config', '-f', '.gitmodules', 'submodule.docs/railspike.url', str(new_remote))
            git(subhost, 'submodule', 'sync', '--', 'docs/railspike')
            git(subhost, 'config', '-f', '.gitmodules', 'submodule.docs/railspike.branch', 'main')
            git(subhost, 'config', 'submodule.docs/railspike.branch', 'main')
            git(sub, 'switch', '--detach', revision_before)
            git(sub, '-c', 'merge.autostash=false', 'merge', '--ff-only', reviewed)

        migrate()
        assert lean(sub) == expected
        assert set(git(subhost, 'diff', '--name-only').splitlines()) == {'.gitmodules', 'docs/railspike'}
        # Roll back only this fixture's owned changes, then prove complete restoration.
        (subhost / '.gitmodules').write_bytes(modules_before)
        git(subhost, 'submodule', 'sync', '--', 'docs/railspike')
        git(subhost, 'config', 'submodule.docs/railspike.branch', 'master')
        git(sub, 'switch', 'master')
        assert git(sub, 'rev-parse', 'HEAD') == revision_before
        assert git(subhost, 'status', '--porcelain') == ''
        assert git(sub, 'remote', 'get-url', 'origin') == str(old_remote)
        migrate()
        git(subhost, 'add', '.gitmodules', 'docs/railspike')
        git(subhost, 'commit', '-qm', 'reviewed source migration')
        run(subhost, 'bash', str(command))
        assert git(subhost, 'status', '--porcelain') == ''
        fresh = root / 'fresh-submodule-host'
        fresh.mkdir()
        git(fresh, 'init', '-q', '--initial-branch=main')
        git(fresh, 'submodule', 'add', source, 'docs/railspike')
        assert lean(fresh / 'docs/railspike') == expected
        assert git(host, 'ls-files', '-s') == index_before
        assert (host / 'work.txt').read_text() == 'unstaged\n'
        print('PASS: remote clone, copied install, actual-history submodule migration,')
        print('      old-source rejection, copy/local-edit preservation, rollback, and host isolation')
        print('Product revision:', current, '; product files:', len(expected))


if __name__ == '__main__':
    main()
