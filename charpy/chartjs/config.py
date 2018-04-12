from charpy.chart import Jsonify


class Config(Jsonify):
    """ config for a chart made with chartjs"""

    def __init__(self, type, data, options):
        self.type = type
        self.data = data
        self.options = options


class Data(Jsonify):
    """ data for a chart made with chartjs"""


class Options(Jsonify):
    """ options for a chart made with chartjs"""


if __name__ == "__main__":  # pragma: no cover
    my_config = Config('bar', [1, 2, 3], {'opt1': 1, 'opt2': ['v1', 'v2']})
    print(my_config.to_json())
