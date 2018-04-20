from flask import render_template
from charpy.chartjs import check_chart_type


class Chart(object):
    def __init__(self, chart_type, legend_display=False, canvas_id='chart'):
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
            self._title_display = True
            self._title = title
        else:
            raise ValueError("Error: Can't set '{}' - an empty String or None to title'".format(title))

    def toggle_legend(self):
        """ toggle the display of the legend between True or False """
        self.legend_display = not self.legend_display

    def add_dataset(self, data_label, data):
        """


        :param data_label: label of the data used for the legend
        :param data:
        :return:
        """
        pass

    def set_canvas_id(self, canvas_id):
        pass

    def render_flask(self, flask_template):
        return render_template(flask_template,
                               script_local=True,
                               id=self.canvas_id,
                               type=self.chart_type,
                               labels=self.labels,
                               datasets=self.datasets.to_json(),
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

    def set_colors(self, backgroundColor, borderColor):
        """

        :param backgroundColor:
        :param borderColor:
        :return:
        """
        self.backgroundColor = backgroundColor
        self.borderColor = borderColor

    def to_json(self):
        dict_dataset = ''

        #import json

        #return json.dump(dict_dataset)


class LineDataset(Dataset):
    def set_color_param(self, fill=False, showLine=True):
        """

        :param fill: fill of backgroundColor between line and x axe
        :param showLine: Show the line in between points for a line chart.
        :return:
        """
        pass