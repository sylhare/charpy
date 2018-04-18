
class Render(object): # pragma: no cover
    """ To render the chart """

    def __init__(self):
        pass

    def to_chartjs(self):
        pass


class Jsonify(object): # pragma: no cover
    """ .. """

    def to_json(self, indent=0):
        """

        :return: a json string of the object
        """
        import json

        return json.dumps(self.__dict__, indent=indent)
