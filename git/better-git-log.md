# A better Git log

Git log usually shows up more information than needed for a quick glance of the commit history. To view a pretty-printed tree structure of the commit tree with the position of all the branches, we can add the following lines in the `.gitconfig` file:

```bash
[alias]
    lg = log --graph --all --branches --oneline --decorate --prty=format:'%C(yellow)%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'
```

Source: [A better git log](https://coderwall.com/p/euwpig/a-better-git-log)
