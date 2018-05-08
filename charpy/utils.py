import os
from charpy import README_RST_PATH, README_MD_PATH
from charpy import ROOT_PATH


def readme_md_to_rst():
    """
    Use pypandoc to create a .rst version of the .md README

    :return: a string with the rst
    """
    try:
        import pypandoc
        result = pypandoc.convert_file(README_MD_PATH, 'rst')

    except ImportError:
        with open(README_MD_PATH) as f:
            result = f.read()
        import warnings
        warnings.warn("Could not convert to rst because pypandoc could not be imported", ImportWarning)

    return result


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