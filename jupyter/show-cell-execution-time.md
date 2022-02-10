# Show Execution Time for each Cell

To show the execution time of each cell in a Jupyter Notebook, we can use the following command in any cell and every cell executed thereafter would have the execution time printed after it.

```python
try:
    %load_ext autotime
except:
    !pip install ipython-autotime
    %load_ext autotime
```

Source: https://stackoverflow.com/a/66931419/10307491
