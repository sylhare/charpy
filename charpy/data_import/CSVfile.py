import csv
from charpy.data_import.converter import transpose, string_to_date, string_to_float


class CSVfile:
    """
    CSVfile class to handle operation on an open csv file
    """
    ROW = "ROW"
    COLUMN = "COLUMN"

    def __init__(self, file, delimiter=None, has_header=None):
        """
        Initialize class with a csv file

        :param file: the open csv file
        :param dialect: optional, default ','
        :param encoding: optional, default 'utf8'
        """
        self.f = file
        self.sniffer = csv.Sniffer()
        self.delimiter = delimiter
        self.has_header = has_header
        self.data_header = None
        self.data_rows = []
        self.data_columns = []
        self.__extract_csv_data()

    def __check_delimiter(self):
        """
        Check if delimiter ',' or ';'

        :return: the dialect (delimiter to open the file)
        """
        if self.delimiter is None:
            self.delimiter = self.sniffer.sniff(self.f.readline(), [',', ';'])
            self.f.seek(0)

    def __check_header(self):
        """
        If not specified, will check if there is a header in the data, otherwise take the given data

        :return:
        """
        if self.has_header is None:
            self.has_header = self.sniffer.has_header(self.f.read(2048))
            self.f.seek(0)

    def __read(self):
        """
        Read the file and return a csv object

        :return:
        """
        self.__check_delimiter()
        reader = csv.reader(self.f, self.delimiter)
        print(reader)
        return reader

    def __extract_csv_data(self):
        """
        Extract the data from the csv file
        If it has a header the value goes to header and the rest to data,
        if not all is assigned to data

        :return: a list of rows
        """
        self.__check_header()
        raw_csv = list(self.__read())  #TODO do not handle if unicode (from ascii to utf-8)

        if self.has_header:
            self.data_header = raw_csv[0]
            self.data_rows = raw_csv[1:]
        else:
            self.data_rows = raw_csv

        self.data_columns = transpose(self.data_rows)

    def get_values(self, data_format=COLUMN):
        """ Get the data from the csv file """
        if data_format == self.ROW:
            return self.data_rows
        else:
            return self.data_columns

    def column_date_format(self, column_number, formatting='%d/%m/%Y'):
        """
        Convert the column string values to another format

        :param formatting: date format
        :param column_number: from 0 to x, which the formatting will be applied to
        """
        pass
        #map(lambda x: string_to_date(x).strftime(formatting), self.data_columns[column_number])

