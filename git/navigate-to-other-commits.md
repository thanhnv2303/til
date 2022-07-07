# Navigating to other commits

**To go to a specific commit in the reflog history:**

Like the terminal saves a history of all the commands executed in the past, Git also saves a log of where our HEAD and branch references have been for the past few months. This information cna be viewed using the command `git reflog`.

```bash
# To go to the fifth last commit in the reflog
git checkout HEAD@{5}
# To go to the last commit where our HEAD was yesterday in the reflog
git checkout@{yesterday}

# NOTE:
# When using PowerShell, braces like { and } are special
# characters and must be escaped. We can escape them with
# a backtick ` or put the commit reference in quotes.
```

**To get to the immediate parent of the current commit:**

```bash
git checkout HEAD^
# OR
git checkout HEAD~
```

**To get back some commits in ancestry:**

```bash
# To get back to parent of parent of parent of current commit
git checkout HEAD~3
# So to get parent of parent of ... n-times of the current commit
git checkout HEAD~n
```

**To go to some nth parent of the current commit:**

The following syntax is useful only for merge commits, which have more than one parent — the **first parent** of a merge commit is from the branch we were on when you merged (frequently `main`), while the **second parent** of a merge commit is from the branch that was merged (say, `topic`):

```bash
# To get back to the 2nd parent of the current commit
git checkout HEAD^2
# To get back to the nth parent of the current commit
git checkout HEAD^n

# NOTE:
# On Windows in cmd.exe, ^ is a special character and needs
# to be treated differently. We can either double it or put
# the commit reference in quotes.
```

So, to get back to the 2nd parent of 3 commits behind HEAD, we can use:

```bash
git checkout HEAD~3^2
```

And to get back 3 commits behind the 2nd parent of HEAD, we can use:

```bash
git checkout HEAD^2~3
```

Source: [Git - Revision Selection](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection)
