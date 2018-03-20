import os
import io
import csv
from charpy.data_import.converter import csv_transpose
from charpy import ROOT_PATH


def get_readme_rst():
    """
    Read the README.rst file and return a string with it content

    :return: README.rst in a string
    """
    readme_path = os.path.join(ROOT_PATH, "README.rst")
    with open(readme_path, 'r') as f:
        readme = f.readlines()

    return ''.join(readme)


def get_csv_data(path):
    """
    Return each row of the csv file

    :param path:
    :return:
    """
    with io.open(path, 'r', encoding='utf8') as f:
        reader = csv.reader((x.replace(u"\uFEFF", u"") for x in f))
        # column_label = list(reader)[0]
        rows = list(reader)

    return rows


def get_demo_data():
    """
    Get the demo data from here (3 level below root) to ./data/demo.csv

    :return: the transpose value of the demo file.
    """
    demo_file_path = os.path.join(ROOT_PATH, os.path.join("data", "demo.csv"))

    value = get_csv_data(demo_file_path)[1:]

    return csv_transpose(value)


if __name__ == "__main__":
    get_readme_rst()
