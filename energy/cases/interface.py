import pandas as pd

import config
import energy.cases.solarcapacity
import energy.cases.windcapacity


class Interface:

    def __init__(self):
        """

        """

        configurations = config.Config()
        uri = configurations.uri

        self.solarcapacity = energy.cases.solarcapacity.SolarCapacity(uri=uri)
        self.windcapacity = energy.cases.windcapacity.WindCapacity(uri=uri)

    def exc(self, tab: str) -> pd.DataFrame:
        """

        :param tab:
        :return:
        """

        if tab == 'solarcapacity':
            return self.solarcapacity.exc()
        elif tab == 'windcapacity':
            return self.windcapacity.exc()
        else:
            raise Exception("If tab '{}' exists, an algorithm has not been implemented for the tab yet".format(tab))
