import math


def color_based_on_sign(data, color_positive="green", color_negative="red"):
    """

    :param data:
    :param color_positive:
    :param color_negative:
    :return:
    """
    color_associated = color_based_on_operation(data, is_positive(), color_positive,
                                                color_negative)

    return color_associated


def color_based_on_value(data, matching_value, color_value="blue", color_not_value="lightgray"):
    color_associated = color_based_on_operation(data, is_equal(matching_value), color_value,
                                                color_not_value)

    return color_associated


def color_based_on_operation(data, matching_criteria, matching_color, not_matching_color):
    """

    :param data:
    :param matching_criteria:
    :param matching_color:
    :param not_matching_color:
    :return:
    """
    color_associated = list(map(lambda x: matching_color if matching_criteria(x) else not_matching_color, data))

    return color_associated


def is_positive():
    """
    :return: a function that determines if the number passed is positive or not
    """
    return lambda x: True if x >= 0 else False


def is_equal(matching_value):
    """
    :param matching_value:
    :return: return a function that determines if the number passed is equat to the matching value that was passed
    """
    return lambda x: True if x == matching_value else False


def color_rainbow(data):
    """

    :param data: a data array
    :return: an array of hex color based on the size of the data array
    """
    rainbow = []
    size = len(data)

    for e in range(size):
        red = sin_to_hex(e, 0, size)
        blue = sin_to_hex(e, 2 * math.pi / 3, size)
        green = sin_to_hex(e, 4 * math.pi / 3, size)
        rainbow.append("#" + red + green + blue)

    return rainbow


def sin_to_hex(x, theta, number_of_taint):
    sin_value = math.sin(2 * math.pi * x / number_of_taint + theta)
    rgb_color = math.floor(sin_value * 127) + 128
    hex_color = format(rgb_color, "x")

    return hex_color if len(hex_color) == 2 else "0" + hex_color


if __name__ == "__main__":  # pragma: no cover
    data_array = [1, -1, 1, -1]
    print(color_based_on_sign(data_array))
    print(color_based_on_value(data_array, matching_value=1))

    print(is_positive()(1))
    print(is_equal(2)(1))

    print(sin_to_hex(0, 0, 20))
    print(color_rainbow(data_array))
