# Split branch by files modified

Ideally a feature branch should contain solving a single issue. If a branch has many commits covering multiple issues, it would be much better (and cleaner) to split that branch into multiple branches. One distinction to split branches can be through the specific files it modifies.

Suppose the branch with many commits is the `very-large-branch` and it needs to be merged into `main`. We divide `very-large-branch` into `split-branch-1` and `split-branch-2`.

To split a branch into separate branches based on files modified:

```bash
# Create a new branch `split-branch-1` from `main`
git checkout -b split-branch-1 main

# Get a list of all commits between `main` and `split-branch-1`
# in chronological order ignoring any
# merge commit that contains changed done in the specified files
# Then sends it to the cherry pick command that
# apply them into the `split-branch-1` branch
git rev-list --reverse --no-merges main..very-big-branch -- \
  <list of files to keep on the first branch> | git cherry-pick --ff --stdin
```

The same can be repeated for the second branch to get out changes from the `very-large-branch` into two separate branches based on files changed.

NOTE: There may be some minor merge conflicts while cherry picking the commits. These can be resolved manually.

Source: [Splitting a git branch by files modified](https://www.flakery.org/splitting-a-git-branch-by-files-modified/)
