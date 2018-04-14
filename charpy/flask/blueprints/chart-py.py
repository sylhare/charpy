from flask import Blueprint, render_template
import os
from charpy.cruncher import Orc
from charpy import MOCK_PATH

bp = Blueprint('charpy', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/charpy')
def chart_demo():
    demo = Orc(os.path.join(MOCK_PATH, "pcbanking.csv"))
    return render_template('chart-py.html', values=demo.df['value'], labels=demo.df['label'], type='pie')


@bp.route("/static")
def chart_static_demo():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC", "#BCAFED"]
    return render_template('chart.html', values=values, labels=labels, set=zip(values, labels, colors))


@bp.route("/hello/<string:name>/")
def hello(name):
    return "hello " + name + "!"
