# Adding file from Drive

To add a file from Drive to your Google Colab notebook, the following commands can be used:

```py
from google.colab import drive
drive.mount('/content/drive')

with open('/content/drive/My Drive/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')
```
