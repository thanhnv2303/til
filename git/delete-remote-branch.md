# Delete remote and local remote-tracking branch

To delete a local branch, `git branch -d <branch-name>` (or with `-D` to force remove unmerged branches) works. However, it won't delete the remote branch, or the local remote-tracking branch.

To delete a remote branch:

```bash
git push <remote> -d <branch-name>  # Git version 1.7.0 or newer
git push <remote> :<branch-name> # Git versions older than 1.7.0
```

To delete local remote-tracking branch:

```bash
git branch -dr <remote>/<branch> # -d for delete, -r for remote
```

To delete multiple obsolete remote-tracking branches:

```bash
git fetch <remote> --prune
```

Source: [How do I delete a Git branch locally and remotely?](https://stackoverflow.com/a/23961231/10307491)
