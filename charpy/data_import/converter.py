from charpy.data_import import README_RST_PATH, README_MD_PATH


def readme_md_to_rst():
    """Use pypandoc to create a .rst version of the .md README """
    try:
        import pypandoc
        result = pypandoc.convert(README_MD_PATH, 'rst')

    except(IOError, ImportError):
        result = open(README_MD_PATH).read()

    return result


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


def csv_to_json(path): # pragma: no cover
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


if __name__ == "__main__":  # pragma: no cover
    print(readme_md_to_rst())
    pass
