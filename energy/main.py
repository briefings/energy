import logging
import os
import sys

import pandas as pd


def main():
    """

    :return:
    """

    # Directories
    energy.algorithms.directories.Directories().exc()

    # Interface
    interface = energy.cases.interface.Interface()

    # The data.  In future use Dask.
    tabs = ['solarcapacity', 'windcapacity']
    readings = []
    for tab in tabs:
        # In focus
        logger.info('\nAnalysing -> \'{}\''.format(tab))
        series = interface.exc(tab=tab)
        readings.append(series)

    # Concatenate
    series: pd.DataFrame = pd.concat(readings, axis=0, ignore_index=True)
    series.to_csv(path_or_buf=os.path.join(configurations.warehouse, 'capacity.csv'), header=True,
                  index=False, encoding='UTF-8')


if __name__ == '__main__':
    """
    Preparing
    
    """

    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'options'))

    # Logging
    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import config
    import energy.algorithms.directories
    import energy.cases.interface

    # Instances
    configurations = config.Config()

    # Hence
    main()
