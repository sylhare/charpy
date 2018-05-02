import json
from flask import render_template
from charpy.chartjs import *


class Chart(object):
    def __init__(self, chart_type, legend_display=False, canvas_id='chart'):
        self.canvas_id = canvas_id
        self.chart_type = check_chart_type(chart_type)
        self._labels = []
        self.datasets = ''

        try:
            self._legend_display = JS_CONVERT[legend_display]
        except KeyError:
            raise ValueError("legend_display, can only accept True or False - input: '{}'".format(legend_display))

        self._title = ''
        self._title_display = JS_CONVERT[False]

    @property
    def title(self):
        """ title require a setter and a getter so a property was creater """

    @title.setter
    def title(self, title):
        """
        Set _title.display to 'true' the javascript value for True
        When the title is set.

        """
        if title is not None and title != '':
            self._title_display = JS_CONVERT[True]
            self._title = title
        else:
            raise ValueError("Error: Can't set '{}' - an empty String or None to title'".format(title))

    @title.getter
    def title(self):
        """ Return the title if it is displayed """
        if PYTHON_CONVERT[self._title_display]:
            return self._title
        else:
            return None

    @property
    def labels(self):
        """ title require a setter and a getter so a property was created """

    @labels.setter
    def labels(self, labels):
        if isinstance(labels, list):
            self._labels = labels
        else:
            raise TypeError("Labels can only be list - not '{}'".format(labels))

    @labels.getter
    def labels(self):
        return self._labels

    def toggle_legend_display(self):
        """
        toggle the display of the legend between 'true' or 'false'
        which are the javascript equivalent for True and False.

        Then return the legend display value into python Boolean.

        """
        self._legend_display = JS_CONVERT[not PYTHON_CONVERT[self._legend_display]]
        return PYTHON_CONVERT[self._legend_display]

    def add_simple_dataset(self, data_label, data):
        """


        :param data_label: label of the data used for the legend
        :param data:
        :return:
        """
        dataset_json = json.dumps({"label": data_label, "data": data})
        self.add_dataset(dataset_json)

    def add_dataset(self, dataset_json):
        """
        Add a dataset from a dataset object

        :param dataset_json:
        :return:
        """
        self.datasets += dataset_json + ","

    def render_html(self):
        """
        Generate an html page of the chart.

        :return: full html page
        """
        return HTML.format(self.title, SCRIPT, self.render_chart_html())

    def render_chart_html(self):
        """
        Render the html part of one chart

        :return: the chart in html
        """
        return CANVAS.format(self.canvas_id) + CHARTJS.format(self.canvas_id,
                                                              self.chart_type,
                                                              self.labels,
                                                              self.datasets,
                                                              self._legend_display,
                                                              self._title_display,
                                                              self.title)

    def render_flask(self, flask_template):
        """
        Use flask and the jinja2 templating system to render the chart

        :param flask_template:
        :return: rendered page
        """
        return render_template(flask_template,
                               script_local=True,
                               id=self.canvas_id,
                               type=self.chart_type,
                               labels=self.labels,
                               datasets=self.datasets,
                               legend_display=self._legend_display,
                               title_display=self._title_display,
                               title=self.title
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


class LineDataset(Dataset):  # pragma: no cover

    def __init__(self, data, label, fill=False, showLine=True):
        super().__init__(data, label)
        self.fill = fill
        self.showLine = showLine
