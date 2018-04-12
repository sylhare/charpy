
class Render(object):
    """ To render the chart """

    def __init__(self):
        pass

    def to_chartjs(self):
        pass


class Jsonify(object):
    """ .. """

    def to_json(self, indent=4):
        """

        :return: a json string of the object
        """
        import json

        return json.dumps(self.__dict__, indent=indent)
