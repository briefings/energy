## Capacity, etc.

<br>

* [Development Notes](#development-notes)
* [References](#references)

<br>

### Development Notes

<br>

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
    
    # For Excel
    conda install -c anaconda xlrd
    
    # For Bayesian Modelling
    conda install -c anaconda pymc3
    
    # For Modelling
    conda install -c anaconda scikit-learn
    
    # Graphing Packages
    conda install -c anaconda matplotlib
    conda install -c anaconda seaborn
    
    # The next line updates scikit-learn: 0.23.2 -> 0.24.2
    pip install -U imbalanced-learn==0.8.0
	
    # For shell script verification
    pip install shellcheck-py==0.7.2.1

    # For Modelling
    pip install yellowbrick==1.3.post1

```

For more about Dask, refer to https://docs.dask.org/en/latest/install.html

<br>

**Updates**

```bash
    conda install -c anaconda pillow==8.3.0
    
```


<br>

**Requirements**

```bash
    conda activate miscellaneous
    pip freeze -r docs/filter.txt > requirements.txt
```

<br>
<br>

### References

* Time Series Analysis
  * [Python datetime.datetime.strptime](https://docs.python.org/3.7/library/datetime.html#datetime.datetime.strptime)
  * [Numpy datetime ](https://numpy.org/doc/stable/reference/arrays.datetime.html)
  * [Pandas time series functios](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
