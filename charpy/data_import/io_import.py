import os
import io
import csv
from charpy.data_import.converter import transpose, readme_md_to_rst, README_RST_PATH
from charpy.data_import.CSVfile import CSVfile
from charpy import DATA_PATH, ROOT_PATH


def create_readme_rst():
    """
    create the readme rst
    """
    result = readme_md_to_rst()
    with open(README_RST_PATH, 'w') as f:
        f.write(result)


def get_readme_rst():
    """
    Read the README.rst file and return a string with it content
    :return: README.rst in a string
    """
    readme_path = os.path.join(ROOT_PATH, "README.rst")
    with open(readme_path, 'r') as f:
        readme = f.read()

    return readme


def get_csv_data(path, transposed=False, encoding='utf8'):
    """
    Return each row of the csv file

    :param encoding: encoding of the file
    :param transposed: if you want the csv data transposed or not
    :param path: of the csv file to get data from
    :return:
    """
    with io.open(path, 'r', encoding=encoding, newline='') as f:
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(f.readline(), [',', ';'])
        f.seek(0)
        # reader = csv.reader(map(lambda x: x.replace(u"\uFEFF", u""), f), dialect)
        reader = csv.reader((x.replace(u"\uFEFF", u"") for x in f), dialect)
        # column_label = list(reader)[0]
        rows = list(reader)

    return transpose(rows) if transposed else rows


def get_demo_data():
    """
    Get the demo data from here (3 level below root) to ./data/demo.csv

    :return: the transpose value of the demo file.
    """
    demo_file_path = os.path.join(DATA_PATH, "demo.csv")
    value = get_csv_data(demo_file_path)[1:]

    return transpose(value)


if __name__ == "__main__":  # pragma: no cover
    create_readme_rst()
    # print(get_readme_rst())
    pass
