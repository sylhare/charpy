import os
from charpy.data_import import README_RST_PATH
from charpy.data_import.converter import readme_md_to_rst
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


if __name__ == "__main__":  # pragma: no cover
    create_readme_rst()
    # print(get_readme_rst())
    pass
