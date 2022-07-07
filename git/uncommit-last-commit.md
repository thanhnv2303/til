# Uncommit last commit

Since there's a no direct meaning of 'uncommit' in git, I'll use the term here to mean **moving changes from the last commit to the staging area**.

To move the changes done in the last commit to the staging area:

```bash
git reset --soft HEAD^
```

**Additionally after this 'uncommit', we may be interested to do the following operations:**

-   To remove a file from the staging area to the working directory:
    ```bash
    git reset HEAD /file/to/delete
    ```

-   To remove a file file from the staging area **and also the index** (i.e. tell git not to track it):
    ```bash
    git rm --cached /file/to/delete
    ```

Source: [Remove files from Git commit](https://stackoverflow.com/a/72024194/10307491)
