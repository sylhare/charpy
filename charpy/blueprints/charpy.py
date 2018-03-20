from flask import Blueprint, render_template

bp = Blueprint('charpy', __name__, template_folder='templates')


@bp.route("/")
def chart_demo():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC", "#BCAFED"]
    return render_template('chart.html', values=values, labels=labels, set=zip(values, labels, colors))