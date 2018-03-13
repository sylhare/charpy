import csv
import json
import io
import pypandoc
import os


def readme_to_rst():
    parent_path = os.path.dirname(os.getcwd())
    readme_md_path = os.path.join(parent_path, os.path.join("docs", "README.md"))
    readme_rst_path = os.path.join(parent_path, "README.rst")
    pypandoc.convert(readme_md_path, 'rst', outputfile=readme_rst_path)


def csv_to_json(path):
    """
    Convert the csv file into a json file while removing '/uFEFF' unicode character for space

    :param path: path of the csv file
    :return: print the json folder with same name in same directory
    """
    with io.open(path, 'r', encoding='utf8') as f:
        reader = csv.DictReader((x.replace(u"\uFEFF", u"") for x in f))
        rows = list(reader)

    with open(path[:-3]+"json", 'w', encoding='utf8') as f:
        f.write(json.dumps(rows, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False))


def get_demo_data():
    """
    Will return the csv rows into column list:
    label_A label_B
       1      4
       2      5
       3      6

    Will return
    [(label-A, 1, 2, 3), (label-B, 4, 5, 6)]

    Test value
    [('labels', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'),
    ('values', '10', '9', '8', '7', '6', '4', '7', '8'),
    ('colors', '#F7464A', '#46BFBD', '#FDB45C', '#FEDCBA', '#ABCDEF', '#DDDDDD', '#ABCABC', '#BCAFED')]

    :param path:
    :return:
    """
    parent_path = os.path.abspath(os.path.dirname(__file__))
    demo_file_path = os.path.join(parent_path, "demo.csv")

    with io.open(demo_file_path, 'r', encoding='utf8') as f:
        reader = csv.reader((x.replace(u"\uFEFF", u"") for x in f))
        # column_label = list(reader)[0]
        rows = list(reader)[1:]
        print(list(zip(*rows)))

    return zip(*rows)


if __name__ == "__main__":
    # csv_to_json("demo.csv")
    # get_demo_data()
    # readme_to_rst()
    print(os.path.abspath(os.path.dirname(__file__)))
    pass
