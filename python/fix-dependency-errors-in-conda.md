# Fix Dependency Errors in Conda

While updating Conda packages, one can often run into dependency errors caused by conflicting packages. Most of these errors can be solved by updating the `.condarc` file with the following lines:

```yaml
ssl_verify: true
channels:
    - defaults
    - conda-forge
channel_priority: flexible
```
