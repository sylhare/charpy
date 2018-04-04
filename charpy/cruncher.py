import os
import pandas as pd
import re
from dateutil.parser import parse
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

    # TODO check the formatting is a correct time formatting
    def format_column_date(self, column, formatting="%d/%m/%Y", dayfirst=True):
        """
        Format a column into a date format

        :param dayfirst: True for the parsing method
        :param formatting:
        :param column:
        :return:
        """
        c = self.__check_column(column)
        if c:

            self.df[c] = list(map(lambda x: parse(x, dayfirst=dayfirst).date().strftime(formatting), self.df[c]))

    def format_column_list(self, column, regex=r'  +'):
        """

        :param c: column to apply
        :param regex: by default more than two spaces
        :return:
        """

        c = self.__check_column(column)
        if c:

            self.df[c] = list(map(lambda x: re.split(regex, x), self.df[c]))

    def __check_column(self, column):
        """
        Column can be a number of a name

        :param column:
        :return: the column name
        """

        try:
            if int == type(column):
                c_name = self.df.columns[column]
            elif column in self.df:
                c_name = column
            else:
                raise TypeError("Error: column should be the number or the name of the column")

        except TypeError as error:
            print(error)
            c_name = False

        return c_name


if __name__ == "__main__":  # pragma: no cover
    s = Orc(os.path.join(DATA_PATH, "pcbanking.csv"))
    print(s.df)
    s.format_column_date("date")
    print(s.df)
    for value in s.df['label']:
        print(re.split(r'  +', value))
