# Undo changes of last commit

**Related: [Uncommit last commit](uncommit-last-commit.md)**

Since there's a no direct meaning of 'undo' for a commit in Git, I'll use the term here to mean **reverting changes done in previous commit by a new commit**.

To revert the changes done in the last commit by a new commit:

```bash
git revert HEAD
```

Alternatively, **to undo changes of only some files** of the last commit, the following command would restore the specified files in the working directory back to the the specified commit:

```bash
git restore --source=HEAD^ files/to/undo
```

Then, a commit would commit the changes to the tree.

Source: [git restore](https://www.git-tower.com/learn/git/commands/git-restore), [Git - git-restore Documentation](https://git-scm.com/docs/git-restore)
