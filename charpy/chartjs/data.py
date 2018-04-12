from charpy.chart import Jsonify

data_number = [20, 10]
data_point = [{'y': 20, 'x': 10}, {'y': 10, 'x': 15}]


class Data(Jsonify):
    """ data for a chart made with chartjs"""

    def __init__(self, label, dataset):
        self.label = label  # "x label"
                            # What about data_point with x and y ?

        if dataset:
            self.dataset = ['dataset-1', 'dataset-2']
        else:
            self.data = data_number



class Dataset(Jsonify):
    """ data for a chart made with chartjs"""

    def __init__(self, label, data):
        self.label = label  # label of the dataset
        self.data = data_number
        self.fillColor = "rgba(151,187,205,0.2)",
        self.strokeColor = "rgba(151,187,205,1)",
        self.pointColor = "rgba(151,187,205,1)",
