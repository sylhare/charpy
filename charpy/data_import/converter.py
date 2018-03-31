from dateutil.parser import parse
from charpy.data_import import README_MD_PATH


def readme_md_to_rst():
    """
    Use pypandoc to create a .rst version of the .md README

    :return: a string with the rst
    """
    try:
        import pypandoc
        result = pypandoc.convert_file(README_MD_PATH, 'rst')

    except(IOError, ImportError):
        result = open(README_MD_PATH).read()

    return result


def transpose(csv_list):
    """
    Transpose a list of rows into a list of columns

    example:
       [['x', 3], ['y', 4], ['z', 5]]

    will become:
       [['x', 'y', 'z'], [3, 4, 5]]

    :return: a transposed list of list
    """
    transposed = map(list, zip(*csv_list))

    return list(transposed)


def string_to_date(string):
    """
    The date returned is a datetime.datetime object

    No need to specify the format:
    date.year gives the year
    date.month gives the month
    date.day gives the day

    the '.date()' remove the hours.

    :param string:
    :return: the date
    """
    return parse(string).date()


def string_to_float(string):
    """
    return a float from a string

    :param string:
    :return: float
    """
    return float(string)


if __name__ == "__main__":  # pragma: no cover
    # print(readme_md_to_rst())
    string_to_date("29/10/2018")
    pass
