# Supplemental immutable evidence

[Entry](./README.md)

## C017 fixture coverage

Read-only inspection: `git -C /home/wsl/fdp show afa08dbdf45f117deda5b2ca8c3c7ef2c78af4d3:scripts/check-fdp-git-workflow.sh`. Blob SHA-256: `b5895bb2462930e8b2bbaad1d8c9d42abd71a3c7d0ed71709b1b3745bed06144`. The full 65-line fixture was inspected; excerpt below retains the dirty-state portion (original lines 60–65). No script was executed.

> pointer_before=&quot;$(git -C &quot;$host&quot; ls-files -s docs/fdp)&quot;
> printf &#x27;dirty\n&#x27; &gt;&quot;$host/docs/fdp/dirty.txt&quot;
> test -n &quot;$(git -C &quot;$host/docs/fdp&quot; status --porcelain)&quot;
> test &quot;$(git -C &quot;$host&quot; ls-files -s docs/fdp)&quot; = &quot;$pointer_before&quot;
>
> printf &#x27;FDP Git workflow fixture passed.\n&#x27;

The preceding fixture performs clean add, clone initialization and fast-forward update. The dirty portion detects state and compares the index pointer without attempting the documented update/refusal path. It supports a narrower assertion than complete refusal/recovery coverage.
