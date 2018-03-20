import os
import pypandoc
from charpy import ROOT_PATH


def readme_md_to_rst():
    readme_md_path = os.path.join(ROOT_PATH, os.path.join("docs", "README.md"))
    readme_rst_path = os.path.join(ROOT_PATH, "README.rst")
    pypandoc.convert(readme_md_path, 'rst', outputfile=readme_rst_path)


def csv_transpose(csv_list):
    """

    example:
    [('x', 3), ('y', 4), ('z', 5)]

    will become
    [('x', 'y', 'z'), (3, 4, 5)]

    :return:
    """
    transpose = zip(*csv_list)

    return list(transpose)


if __name__ == "__main__":
    readme_md_to_rst()
