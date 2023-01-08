# Merge a remote branch without checkout

If we are checked out on a branch and want to merge a remote branch to some different branch without leaving the current branch, we can do the following:

```bash
git fetch <remote> <sourceBranch>:<destinationBranch>
```

Here, we are fetching the remote branch `<sourceBranch>` from `<remote>` and merging it to `<destinationBranch>`.

`sourceBranch` and `destinationBranch` can be the same. For example, if you are checked out on `develop` and want to merge remote updates from `master` to `develop` without leaving `develop`, you can do the following:

```bash
git fetch origin master:master
git merge master
```

Source: [Merge, update, and pull Git branches without using checkouts](https://stackoverflow.com/a/17722977)
