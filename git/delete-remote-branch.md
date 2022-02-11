# Delete Remote Branch

To delete a local branch, `git branch -D <branch-name>` works but if the branch is pushed to remote, then it would still remain there.

To delete a remote branch at `origin`. we can use the following command

```bash
git push origin :<locally-deleted-branch-name>
```
