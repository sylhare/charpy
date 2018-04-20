import json
from flask import render_template
from charpy.chartjs import check_chart_type

# TODO False is false in javascript /!\ to implement
class Chart(object):
    def __init__(self, chart_type, legend_display='false', canvas_id='chart'):
        self.canvas_id = canvas_id
        self.chart_type = check_chart_type(chart_type)
        self.labels = []
        self.datasets = None
        self.legend_display = legend_display
        self._title = ''
        self._title_display = False

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        """ Need to set display to true """
        if title is not None and title != '':
            self._title_display = 'true'
            self._title = title
        else:
            raise ValueError("Error: Can't set '{}' - an empty String or None to title'".format(title))

    #TODO update toggle_legend to be javascript compatible
    def toggle_legend(self):
        """ toggle the display of the legend between True or False """
        self.legend_display = not self.legend_display

    def add_dataset(self, data_label, data):
        """


        :param data_label: label of the data used for the legend
        :param data:
        :return:
        """
        self.datasets = {"label": data_label, "data": data}
        print(self.datasets)

    def render_flask(self, flask_template):
        print(self.datasets)
        return render_template(flask_template,
                               script_local=True,
                               id=self.canvas_id,
                               type=self.chart_type,
                               labels=self.labels,
                               datasets=self.datasets,
                               legend_display=self.legend_display,
                               title_display=self._title_display,
                               title=self._title
                               )


class Dataset(object):
    def __init__(self, data, label=''):
        self.label = label
        self.data = data
        self.backgroundColor = "royalBlue"
        self.borderColor = "white"

    def set_label(self, label):
        if type(label) == str:
            self.label = label
        else:
            raise TypeError("Error: The label should be a string - input '{}'".format(label))

    def set_data(self, data):
        if type(data) == list:
            self.data = data
        else:
            raise TypeError("Error: data can't be a string - '{}'".format(data))

    def to_json(self):

        return json.dumps(self.__dict__, sort_keys=True, ensure_ascii=False)


class LineDataset(Dataset):

    def __init__(self, data, label, fill=False, showLine=True):
        super().__init__(data, label)
        self.fill = fill
        self.showLine = showLine
