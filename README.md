<br>

## Capacity, etc.

<br>

* [Development Notes](#development-notes)
* [References](#references)

<br>

### Development Notes

<br>

The environment is ``miscellaneous``

```bash
  conda create --prefix .../miscellaneous
  conda activate miscellaneous
```

The set-up includes

```bash
    conda install -c anaconda python==3.8.13
    
    conda install -c anaconda dask==2021.10.0 # installs: numpy, pandas
    conda install -c anaconda python-graphviz # installs: graphviz
    conda install -c anaconda pywin32 jupyterlab nodejs # installs: requests, urllib3
    conda install -c anaconda pytest coverage pylint pytest-cov
    
    # For Excel
    conda install -c anaconda xlrd
	conda install -c anaconda openpyxl
    
    # For Bayesian Modelling
    conda install -c anaconda pymc3
    
    # For Modelling
    conda install -c anaconda scikit-learn
    
    # Graphing Packages
    conda install -c anaconda matplotlib
    conda install -c anaconda seaborn
    
    # imbalanced
    pip install -U imbalanced-learn
	
    # For shell script verification
    pip install shellcheck-py

    # For Modelling
    pip install yellowbrick

```

For more about Dask, refer to https://docs.dask.org/en/latest/install.html. In terms of requirements

```bash
    pip freeze -r docs/filter.txt > requirements.txt
```

<br>
<br>

### References

* Time Series Analysis
  * [Python datetime.datetime.strptime](https://docs.python.org/3.7/library/datetime.html#datetime.datetime.strptime)
  * [Numpy datetime ](https://numpy.org/doc/stable/reference/arrays.datetime.html)
  * [Pandas time series functios](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
