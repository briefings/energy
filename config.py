import os


class Config:

    def __init__(self):
        """
        The constructor
        """

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
        self.uri = os.path.join(os.getcwd(), 'data', 'bp-stats-review-2020-all-data.xlsx')
