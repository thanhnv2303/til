# Uncommit last Commit

There's a no direct command to uncommit the last commit in git. Adding the following line to the `.gitconfig` file can be used to do this:

```bash
[alias]
    uncommit = reset HEAD~
```
