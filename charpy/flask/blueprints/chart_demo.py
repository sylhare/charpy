import os
from charpy.cruncher import Orc
from charpy import MOCK_PATH
from charpy.chartjs import chart, color
from flask import Blueprint, render_template

bp = Blueprint('charpy', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/chart_demo/default/')
def chart_demo():
    demo = Orc(os.path.join(MOCK_PATH, "pcbanking.csv"))
    return render_template('view/chart_demo.html', values=demo.df['value'], labels=demo.df['label'], type='pie')


@bp.route('/chart_demo/static/')
def chart_static_demo():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC", "#BCAFED"]
    return render_template('view/chart_static.html', version="1.0.1", values=values, labels=labels,
                           set=zip(values, labels, colors))


@bp.route('/chart_demo/charpy/')
def chart_chartjs():
    demo = Orc(os.path.join(MOCK_PATH, "pcbanking.csv"))
    chamo = chart.Chart('bar')
    chamo.title = "Test chart from template"
    chamo.add_simple_dataset('value', demo.df['value'].tolist())
    chamo.labels = demo.df['label'].tolist()

    return chamo.render_flask('view/chartjs_default.html')


@bp.route('/chart_demo/two/')
def two_chartjs_demo():
    chamo = chart.Chart('bar')
    chamo.title = "Test chart from template"
    demo = Orc(os.path.join(MOCK_PATH, "pcbanking.csv"))
    chamo.add_simple_dataset('value', demo.df['value'].tolist())
    chamo.labels = demo.df['label'].tolist()

    charts = chamo.render_chart() + chamo.render_chart("pie")

    return chart.Chart.render_raw(charts)


@bp.route('chart_demo/colored')
def colored_chart():
    pass


@bp.route("/chart_demo/hello/<string:name>/")
def hello(name):
    return "hello " + name + "!"
