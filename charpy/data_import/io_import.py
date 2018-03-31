import os
import io
from charpy.data_import import README_RST_PATH
from charpy.data_import.converter import readme_md_to_rst
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


def get_csv_data(path, data_format=CSVfile.COLUMN, encoding='utf8'):
    """
    Return each row of the csv file

    :param encoding: encoding of the file
    :param data_format: if you want the csv data as column or row
    :param path: of the csv file to get data from
    :return:
    """
    with io.open(path, 'r', encoding=encoding, newline='') as f:
        file = CSVfile(f)

    return file.get_values(data_format)


def get_demo_data():
    """
    Get the demo data from here (3 level below root) to ./data/demo.csv

    :return: the transpose value of the demo file.
    """
    demo_file_path = os.path.join(DATA_PATH, "demo.csv")
    value = get_csv_data(demo_file_path)

    return value


if __name__ == "__main__":  # pragma: no cover
    create_readme_rst()
    # print(get_readme_rst())
    pass
