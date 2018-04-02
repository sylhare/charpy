import os
import datetime
from dateutil.parser import parse
import pandas as pd
from charpy import DATA_PATH


class Orc(object):
    """
    Open the file
    Read the data
    Clean it accordingly
    """
    DEFAULT_NAMES = ['date', 'label', 'value']

    def __init__(self, path, sep=None, header=None, names=DEFAULT_NAMES):
        """

        :type names: object
        """
        criteria = {'sep': sep}

        if sep is None:
            criteria['engine'] = 'python'
        if header is None:
            criteria['header'] = None
            criteria['names'] = names
        else:
            criteria['header'] = header

        self.df = pd.read_csv(path, **criteria)

    def format_date(self, column, formatting="%d/%m/%Y"):
        """
        Format a column into a date format

        :param formatting:
        :param column:
        :return:
        """
        try:
            if int == type(column):
                c = self.df.columns[column]
            elif str == type(column):
                c = column
            else:
                raise TypeError("column should be the number or the name of the column")

            self.df[c] = list(map(lambda x: parse(x).date().strftime(formatting), self.df[c]))

        except TypeError as error:
            print(error)


if __name__ == "__main__":  # pragma: no cover
    s = Orc(os.path.join(DATA_PATH, "pcbanking.csv"))
    print(s.df)
    s.format_date("date")
    print(s.df)

