from charpy.chart import Jsonify

data_number = [20, 10]
data_point = [{'y': 20, 'x': 10}, {'y': 10, 'x': 15}]


class Dataset(Jsonify): # pragma: no cover
    """ data for a chart made with chartjs"""

    def __init__(self, label='values', data='data'):
        self.label = label  # label of the dataset
        self.data = ["test", "ee"]

        self.backgroundColor = ''
        self.borderColor = ''
        self.pointBorderColor = ''
        self.pointBackgroundColor = ''
        self.fillColor = "rgba(151,187,205,0.2)"
        self.strokeColor = "rgba(151,187,205,1)"
        self.pointColor = "rgba(151,187,205,1)"


class Data(Jsonify): # pragma: no cover
    """ data for a chart made with chartjs"""

    def __init__(self, label='', input_data=''):
        self.label = label
        self.datasets = Dataset().to_json()
