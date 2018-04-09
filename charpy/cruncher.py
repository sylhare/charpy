import os
import pandas as pd
import re
from dateutil.parser import parse


def check_path(path):
    """ Check if the path is a directory or a file and return a list of the file in the path """
    list_path = []

    try:
        if os.path.isdir(path):
            list_path = list(map(lambda x: os.path.join(path, x), os.listdir(path)))
        else:
            list_path.append(path)

    except TypeError as error:
        print("Error: Input path not valid - path: '{}' - error: {}".format(path, error))

    return list_path


class Orc(object):
    """
    Open the file
    Read the data
    Clean it accordingly
    """
    DEFAULT_NAMES = ['date', 'label', 'value']
    DEFAULT_SUB_NAMES = ['article', 'city', 'province']

    def __init__(self, path, sep=None, header=None, names=DEFAULT_NAMES):
        """

        :param path: Where the file(s) are to be opened
        :param sep: if not specified will be found automatically
        :param header: is
            - 'None' there are no header default header are taken
            - An int, then the row[ int ] will be the header and can't be renamed using name
        :param names: names of the columns
        """
        criteria = {'sep': sep, 'header': header}

        if sep is None:
            criteria['engine'] = 'python'
        if header is None:
            criteria['names'] = names

        self.df = pd.DataFrame()
        self.read_csv(path, criteria)

    def read_csv(self, path, criteria):
        """ Read all of the csv file in the path and add them to the dataframe """
        for file in check_path(path):
            if file.endswith('.csv'):
                self.df = self.df.append(pd.read_csv(file, **criteria), ignore_index=True)

    # TODO check the formatting is a correct time formatting
    def format_column_date(self, column, formatting="%d/%m/%Y", dayfirst=True):
        """
        Format a column into a date format

        :param dayfirst: True for the parsing method
        :param formatting:
        :param column: column to apply
        :return:
        """
        c = self.__check_column(column)
        if c:
            self.df[c] = list(map(lambda x: parse(x, dayfirst=dayfirst).date().strftime(formatting), self.df[c]))

    def format_column_list(self, column, regex=r'  +'):
        """
        Format the column into a list using regex

        :param column: column to apply
        :param regex: by default more than two spaces
        :return:
        """

        c = self.__check_column(column)
        if c:
            self.df[c] = list(map(lambda x: re.split(regex, x), self.df[c]))

    def create_columns_from_list_column(self, column, names=DEFAULT_SUB_NAMES):
        """
        Take a column that has list values and create columns for it

        Add a buffer to the list in case there are not enough elements to create the column
        It will add '' instead

        :return:
        """

        c = self.__check_column(column)
        if c:
            buffer = ['' for i in names]

            try:
                for r in range(len(self.df[c])):
                    if type(self.df.at[r, c]) == list:
                        self.df.at[r, c].extend(buffer)
                    else:
                        raise TypeError('Error: The column needs to only contain list objects')

                for i in range(len(names)):
                    self.df[names[i]] = map(lambda x: x[i], self.df[c])

            except TypeError as error:
                print(error)

    def __check_column(self, column):
        """
        Column can be a number of a name

        :param column:
        :return: the column name
        """
        try:
            if int == type(column):
                if column >= 0:
                    c_name = self.df.columns[column]
                else:
                    raise TypeError("Error: column should be a positive number")

            elif column in self.df:
                c_name = column
            else:
                raise TypeError("Error: column should be the number or the name of the column")

        except TypeError as error:
            print(error)
            c_name = False

        return c_name


if __name__ == "__main__":  # pragma: no cover
    from charpy import DATA_PATH, ROOT_PATH
    Orc(ROOT_PATH)
    s = Orc(os.path.join(DATA_PATH, 'empty'))
    # print(os.listdir(DATA_PATH))
    # s.format_column_date('date')
    # s.format_column_list('label')
    # s.create_columns_from_list_column('label')
    print(s.df)
