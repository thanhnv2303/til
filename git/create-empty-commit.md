# Create an empty commit

By default, Git doesn't alow creating empty commits. There might be situations when an empty commit might be required (such as triggering a new CI build).

To create an empty git commit:

```bash
git commit --allow-empty -m "This is an empty commit"
```
