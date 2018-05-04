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
        dataset_json = json.dumps({"label": data_label, "data": data}, sort_keys=True)
        self.add_dataset(dataset_json)

    def add_dataset(self, dataset_json):
        """
        Add a dataset from a dataset object

        :param dataset_json: Dataset or json
        :return:
        """
        if isinstance(dataset_json, Dataset):
            dataset_json = dataset_json.to_json()

        self.datasets += dataset_json + ","

    @staticmethod
    def render_raw(content, title='', script=SCRIPT):
        """
        Static method to allow to draw a raw HTML which can contain multiple charts

        :param title: default is ''
        :param script: default is __chartjs_version__
        :param content: what goes in the body of the html page
        :return:
        """
        return HTML.format(title, script, content)

    def render_html(self):
        """
        Generate an html page of the chart.

        :return: full html page
        """

        return Chart.render_raw(self.title, SCRIPT, self.render_chart())

    def render_chart(self, chart_type=None):
        """
        Render the html part of one chart
        The chart type can be changed on demand if not a right type, will be default.

        :return: the chart in html
        """

        if chart_type is not None and is_chartjs_type(chart_type):
            chart_type = chart_type
            canvas_id = "id_" + chart_type
        else:
            chart_type = self.chart_type
            canvas_id = self.canvas_id

        return CANVAS.format(canvas_id) + CHARTJS.format(canvas_id,
                                                         chart_type,
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


if __name__ == "__main__":  # pragma: no cover
    chart = Chart('bar')
    d = Dataset(data=[1, 2, 3], label='numbers')
    chart.add_simple_dataset(data_label='numbers', data=[1, 2, 3])
    print(chart.datasets)
    chart.add_dataset(d)
    print(d.to_json())
    print(chart.render_chart())
