import datetime

class Cleaner:

    def __init__(self, datalist):
        """ Initialise the cleaner class with the data to be cleaned in it"""
        self.datalist = datalist

    def remove_label(self):
        pass

    def parse_string_to_date(self, string):

        # if year is two digit -> %y if four digit -> %Y
        datetime.strptime(string, '%d/%m/%y')
        datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
