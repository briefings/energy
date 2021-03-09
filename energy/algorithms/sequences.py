import numpy as np
import pandas as pd

import energy.algorithms.reference


class Sequences:

    def __init__(self):
        """
        The constructor

        """

        self.reference = energy.algorithms.reference.Reference()

    @staticmethod
    def time(blob: pd.DataFrame):
        """


        :param blob:
        :return:
        """

        # Either
        # series.loc[:, 'year'] = series['year'].apply(lambda x: datetime.datetime.strptime(x, '%Y'))
        # series.loc[:, 'year'] = series['year'].astype(dtype='datetime64[Y]')
        # series.loc[:, 'year'] = pd.to_datetime(series['year'], format='%Y')
        series = blob.copy()
        series.loc[:, 'year'] = pd.to_datetime(series['year'], format='%Y')

        # Hence
        series.sort_values(by=['year'], axis=0, ascending=True, inplace=True)
        series.reset_index(drop=True, inplace=True)

        return series

    def discrete(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        # Calculate discrete values regardless of possible missing time points
        series = blob.copy()
        series.loc[:, 'discrete_mw'] = np.diff(a=series['cumulative_mw'], prepend=0, n=1)

        # Ascertaining sequential points in time
        reference: pd.DataFrame = self.reference.exc(starting=series['year'].min(), ending=series['year'].max())

        # Therefore, a frame that does not have missing time points.  The discrete
        # value w.r.t. a missing time point is zero.
        frame = reference.merge(series, how='left', on='year')
        frame.drop(columns=['cumulative_mw'], inplace=True)
        frame.fillna(0, inplace=True)

        return frame

    @staticmethod
    def cumulative(blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        series = blob.copy()
        series.loc[:, 'cumulative_mw'] = series['discrete_mw'].cumsum(axis=0)

        return series

    def exc(self, blob: pd.DataFrame):
        """

        :param blob: Expects frame of year: str, cumulative_mw: float, type: int
        :return:
        """

        # Format and structure the year field values
        series = self.time(blob=blob)

        # Determine the discrete values; of both existing & missing time points
        series = self.discrete(blob=series)

        # Re-calculate the cumulative values
        series = self.cumulative(blob=series)

        return series
