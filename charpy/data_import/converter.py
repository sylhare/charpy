
def csv_to_json():
    """
    Convert a .csv file into a .json file and print it in the data directory

    :return:
    """
    pass


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
