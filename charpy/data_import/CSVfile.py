import csv
from charpy.data_import.converter import transpose


class CSVfile:
    """
    CSVfile class to handle operation on an open csv file
    """

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
        self.extract_csv_data()

    def check_delimiter(self):
        """
        Check if delimiter ',' or ';'

        :return: the dialect (delimiter to open the file)
        """
        if self.delimiter is None:
            self.delimiter = self.sniffer.sniff(self.f.readline(), [',', ';'])
            self.f.seek(0)

    def check_header(self):
        """
        If not specified, will check if there is a header in the data, otherwise take the given data

        :return:
        """
        if self.has_header is None:
            self.has_header = self.sniffer.has_header(self.f.read(2048))
            self.f.seek(0)

    def read(self):
        """
        Read the file and return a csv object

        :return:
        """
        self.check_delimiter()
        reader = csv.reader((x.replace(u"\uFEFF", u"") for x in self.f), self.delimiter)
        return reader

    def extract_csv_data(self):
        """
        Extract the data from the csv file
        If it has a header the value goes to header and the rest to data,
        if not all is assigned to data

        :return: a list of rows
        """
        self.check_header()
        raw_csv = list(self.read())

        if self.has_header:
            self.data_header = raw_csv[0]
            self.data_rows = raw_csv[1:]
        else:
            self.data_rows = raw_csv

        self.data_columns = transpose(self.data_rows)
