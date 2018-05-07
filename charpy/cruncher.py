import os
import re
import pandas as pd
from charpy import DEFAULT_DB_URI
from sqlalchemy import create_engine
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
    Wrapper around a pandas dataframe

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
        """
        Read all of the csv file in the path and add them to the dataframe
        """
        for file in check_path(path):
            if file.endswith('.csv'):
                self.df = self.df.append(pd.read_csv(file, **criteria), ignore_index=True)

    def get_column_values(self):
        """
        :return a list of the values formatted string of each each columns
        """
        str_df = self.df.astype(str)
        return list(map(lambda x: str_df[x].values.tolist(), str_df.columns.values.tolist()))

    # TODO check the formatting is a correct time formatting
    def format_column_date(self, column, formatting="%d/%m/%Y", dayfirst=True):
        """
        Format a column into a date format
        without pd.to_datetime(raw_data['column-name'])

        :param dayfirst: True for the parsing method
        :param formatting: date format to apply
        :param column: column to apply
        """
        c = self.__check_column(column)
        if c:
            try:

                self.df[c] = list(map(lambda x: parse(x, dayfirst=dayfirst).date().strftime(formatting), self.df[c]))
            except (ValueError, TypeError) as error:
                print("Couldn't parse through the dates - {}".format(error))

    def create_from_date_column(self, input_date_column, output_column_name='', formatting='%d/%m/%Y'):
        """
        Create a column with a specific date format from a column where there are dates

        :param input_date_column: source column with date from where you want to create other columns
        :param output_column_name: name of the created column
        :param formatting: date formatting of the output column
                           use regex or simplified notification for day, month or year.
        """

        if output_column_name == '':
            output_column_name = formatting.replace("%", "")

        self.df[output_column_name] = self.df[self.__check_column(input_date_column)]

        if formatting in ("month", "Month", "m", "M"):
            formatting = "%B"
        elif formatting in ("day", "Day", "d", "D"):
            formatting = "%A"
        elif formatting in ("year", "Year", "y", "Y"):
            formatting = "%Y"

        self.format_column_date(output_column_name, formatting=formatting)

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

    def create_from_list_column(self, column, names=DEFAULT_SUB_NAMES):
        """
        Take a column that has list values and create columns for it

        Add a buffer to the list in case there are not enough elements to create the column
        It will add '' instead

        :return:
        """

        c = self.__check_column(column)
        if c:
            empty_buffer = ['' for i in names]

            try:
                for r in range(len(self.df[c])):
                    if type(self.df.at[r, c]) == list:
                        self.df.at[r, c].extend(empty_buffer)
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
                    raise TypeError("TypeError: column should be a positive number")

            elif column in self.df:
                c_name = column
            else:
                raise ValueError("ValueError: column should be the number or the name of the column")

        except (TypeError, ValueError, IndexError) as error:
            print(error)
            c_name = False

        return c_name

    def get_json_data(self, column_name):
        """ Return the json data of a column """
        return self.df[column_name].to_json()

    # TODO change 'replace' by fail and create a backup if enable before retrying with replace
    def create_sql_db(self, name="charpy", db_path=DEFAULT_DB_URI):
        """
        Dump the information of the dataframe into an sql format
        If the sql database has already the same name table it will replace it.

        :param db_path: Path of the database
        :param name - will be the name of the sql table
        """
        engine = create_engine('sqlite:///' + db_path)
        self.df.to_sql(name, engine, if_exists='replace')


if __name__ == "__main__":  # pragma: no cover
    from charpy import MOCK_PATH, ROOT_PATH
    s = Orc(os.path.join(MOCK_PATH, 'pcbanking.csv'))
    # print(Orc(os.path.join(DATA_PATH, "demo.csv")).df)
    s.df['value'] = s.df['value'].astype('float64')
    # print(s.df['value'].dtype)
    # print(os.listdir(DATA_PATH))
    s.format_column_date('date')
    # s.format_column_list('label')
    # s.create_from_list_column('label')
    s.format_column_date('test')
    # print(s.df.to_html())
    s.create_sql_db()



