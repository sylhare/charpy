import io
import csv
import json
from charpy.data_import import README_RST_PATH, README_MD_PATH


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


if __name__ == "__main__":  # pragma: no cover
    print(readme_md_to_rst())
    pass
