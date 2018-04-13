from charpy.chart import Jsonify
from charpy.chartjs.data import *


class Config: # pragma: no cover
    """ config for a chart made with chartjs"""

    def __init__(self, chart_type):
        self.type = chart_type
        self.data = Data().to_json()
        self.options = Options().to_json()

    def to_json(self, indent=4):
        """

        :return: a json string of the object
        """
        import json

        return json.dumps(self.__dict__, indent=indent).replace("\\n", "").replace("\\", "")


class Options(Jsonify): # pragma: no cover
    """ options for a chart made with chartjs"""


if __name__ == "__main__":  # pragma: no cover
    #my_config = Config('bar', [1, 2, 3], {'opt1': 1, 'opt2': ['v1', 'v2']})
    my_config = Config('bar')
    print(type(my_config.to_json()))
