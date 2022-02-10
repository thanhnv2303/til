# Clone GitHub Repo in Colab

To clone a GitHub repository (both private or public) inside a Google Colab Notebook, use the following code:

```python
uname = "<your username>"
!git config --global user.email '<your email>'
!git config --global user.name '<your name>'

from getpass import getpass
password = getpass('Password:')
!git clone https://$uname:$password@github.com/<username>/<repo name>.git
!cd <repo name>
```

NOTE: Somebody who has access to the values in the current variables in the notebook would be able to get the value stored in the `password` variable, so use this carefully.
