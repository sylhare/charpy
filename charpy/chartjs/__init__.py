__chartjs_version__ = "2.7.2"

JS_CONVERT = {True: 'true', False: 'false'}
PYTHON_CONVERT = {'true': True, 'false': False}

LINE = "line"
BAR = "bar"
HORIZONTAL_BAR = "horizontalBar"
RADAR = "radar"
POLAR_AREA = "polarArea"
DOUGHNUT = "doughnut"
PIE = "pie"
BUBBLE = "bubble"
SCATTER = "scatter"

TYPE = {
    LINE,
    BAR,
    HORIZONTAL_BAR,
    RADAR,
    POLAR_AREA,
    DOUGHNUT,
    PIE,
    BUBBLE,
    SCATTER
}


def is_chartjs_type(chart_type):
    """
    Return True if the chart type is handled by chartjs

    :param chart_type:
    :return: True or False
    """
    if chart_type in TYPE:
        return True
    else:
        return False


def check_chart_type(chart_type):
    if is_chartjs_type(chart_type):
        return chart_type
    else:
        raise TypeError("Error: The type '{}' is not a handled chartjs type".format(chart_type))