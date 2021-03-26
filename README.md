### Options

<br>

* [Development Notes](#development-notes)
* [References](#references)

<br>

#### Development Notes

**Environment**

```bash
  conda create --prefix .../miscellaneous
  conda activate miscellaneous
```

Hence

```bash
    conda install -c anaconda python==3.7.7
    
    conda install -c anaconda dask # installs: numpy, pandas
    conda install -c anaconda python-graphviz # installs: graphviz
    conda install -c anaconda pywin32 jupyterlab nodejs # installs: requests, urllib3
    conda install -c anaconda pytest coverage pylint pytest-cov
    
    conda install -c anaconda xlrd
```

For more about Dask, refer to https://docs.dask.org/en/latest/install.html

<br>

**Requirements**

```bash
    conda activate miscellaneous
    pip freeze -r docs/filter.txt > requirements.txt
```

<br>
<br>

#### References

* Time Series Analysis
  * [Python datetime.datetime.strptime](https://docs.python.org/3.7/library/datetime.html#datetime.datetime.strptime)
  * [Numpy datetime ](https://numpy.org/doc/stable/reference/arrays.datetime.html)
  * [Pandas time series functios](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)