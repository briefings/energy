import pandas as pd

import numpy as np


class Reference:

    def __init__(self):
        """
        The constructor

        """

    @staticmethod
    def exc(starting: pd.Timestamp, ending: pd.Timestamp) -> pd.DataFrame:
        """
        In future, add a frequency parameter

        :param starting:
        :param ending:
        :return:
        """

        """
        The approach
        
            sequence = pd.DataFrame(pd.date_range(start=starting, end=ending + pd.Timedelta('1Y'), freq='Y'), 
                                    columns=['year'])
                                    
        has a number of odd behaviours & impacts, hence                                
        """
        array = np.arange(starting, ending + np.timedelta64(1, 'Y'), dtype='datetime64[Y]')
        sequence = pd.DataFrame(data=pd.to_datetime(array), columns=['year'])

        return sequence
