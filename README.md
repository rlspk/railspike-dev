# Railspike development

Plans, debug logs, research, maintainer records, and checks for [Railspike](https://github.com/rlspk/railspike). Install the product repository in consuming projects. Website sources live in [rlspk.github.io](https://github.com/rlspk/rlspk.github.io).

- [Development documentation](./docs/README.md)
- [Feature plans](./docs/plans/README.md)
- [Contributing](./CONTRIBUTING.md)
- [Migration and preservation record](./docs/maintainers/REPOSITORY_SPLIT.md)

## Working on Railspike

Keep separate checkouts of `railspike-dev`, `railspike`, and (when needed) `rlspk.github.io`. Read the product's `RAILSPIKE.md` for its workflow. Railspike's own plans and debug logs belong here in `docs/plans/`, even when implementation edits the product or website checkout. Commit stage summaries here and record paired repository commits before continuing. Consuming projects still keep their own plans in their own `docs/plans/`.

## Checks

The link checkers accept an explicit root and optional exact historical baseline. Choose any installed runtime; when changing shared behavior, run all three. Missing roots, new broken links, and stale baseline entries fail. The baseline is only for preserved research excerpts and references to untracked source material that was not migrated; never apply it to the product.

```bash
python scripts/check-markdown-links.py . docs/maintainers/historical-link-baseline.txt
perl scripts/check-markdown-links.pl . docs/maintainers/historical-link-baseline.txt
node scripts/check-markdown-links.mjs . docs/maintainers/historical-link-baseline.txt

# Replace ../railspike with your product checkout.
python scripts/check-markdown-links.py ../railspike
bash scripts/check-railspike-git-workflow.sh ../railspike
git diff --check

# Python 3: actual product installation and legacy migration/recovery fixtures.
python3 scripts/check-repository-separation.py https://github.com/rlspk/railspike.git b59f7df89842ba17f710ae1f2dc955bb361cc620
```

The Git fixture extracts the exact update block from the selected product README and uses disposable local repositories. It checks initialized and uninitialized submodules, dirty worktrees, unexpected configuration, and unavailable upstreams without changing the selected checkout. The three link checkers remain dependency-free; Python supports 2.7+ and 3.
