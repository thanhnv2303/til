# Consistent LF Endings in Git

Working with Git to sync files across multiple machines (especially Windows and UNIX-based OS) can be a mess with LF line endings by default in UNIX and CRLF line endings by default in Windows.

To ensure that line endings are consistent across all machines, we can add the following line to `.gitattributes` file of the repository to make sure that all files are LF line endings by default:

```bash
* text=auto eol=lf
```
