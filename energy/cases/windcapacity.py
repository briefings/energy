import collections

import numpy as np
import pandas as pd

import energy.algorithms.sequences


# noinspection PyUnresolvedReferences,PyProtectedMember
class WindCapacity:

    def __init__(self, uri):
        """
        Cumulative Installed Capacity, Megawatts

        :param uri:
        """

        # Path
        self.uri = uri

        # Spreadsheet
        Data = collections.namedtuple(typename='Data', field_names=['sheet_name', 'cells', 'start', 'end'])
        self.data = Data._make(('Wind Capacity', 'A:Z', 70, 70))

        FieldNames = collections.namedtuple(typename='FieldNames', field_names=['cells', 'row'])
        self.fieldnames = FieldNames._make(('A:Z', 4))

        # 'wind turbine'
        self.type = 2

        # Instances
        self.sequences = energy.algorithms.sequences.Sequences()

    def dataset(self) -> pd.DataFrame:
        """

        :return:
        """

        try:
            return pd.read_excel(io=self.uri, sheet_name=self.data.sheet_name, header=None,
                                 skiprows=np.arange(self.data.start - 1), usecols=self.data.cells,
                                 nrows=(self.data.end - self.data.start + 1))
        except OSError as err:
            raise Exception(err.strerror) from err

    def fields(self) -> list:
        """

        :return:
        """

        try:
            names = pd.read_excel(io=self.uri, sheet_name=self.data.sheet_name, header=None,
                                  skiprows=self.fieldnames.row - 1, usecols=self.fieldnames.cells, nrows=1,
                                  parse_dates=True)
        except OSError as err:
            raise Exception(err.strerror) from err

        return names.astype(str).values.tolist()[0]

    def restructure(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        # Constructing the frame of a series wherein each instance consists of year, cumulative megawatts value,
        # and generation type
        series = blob.copy().melt(id_vars='Megawatts', var_name='year', value_name='cumulative_mw')
        series = series[series.columns.drop(labels='Megawatts')]
        series.fillna(0, inplace=True)

        # Energy generation type; code.
        series.loc[:, 'type'] = self.type

        return series

    def exc(self) -> pd.DataFrame:
        """

        :return: A frame wherein
        """

        # Data
        data: pd.DataFrame = self.dataset()
        data: pd.DataFrame = data.set_axis(labels=self.fields(), axis=1)
        data: pd.DataFrame = self.restructure(blob=data)
        data: pd.DataFrame = self.sequences.exc(blob=data)

        return data
