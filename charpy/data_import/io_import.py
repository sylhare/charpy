import os
import io
import csv
from charpy.data_import.converter import csv_transpose


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
    parent_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    demo_file_path = os.path.join(parent_path, os.path.join("data", "demo.csv"))

    value = get_csv_data(demo_file_path)[1:]

    return csv_transpose(value)


if __name__ == "__main__":
    get_demo_data()