from flask import Flask
from flask import render_template
from charpy import toolbox

app = Flask(__name__)


@app.route("/")
def chart_demo():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC", "#BCAFED"]
    return render_template('chart.html', values=values, labels=labels, set=zip(values, labels, colors))


@app.route("/chart")
def chart_file():
    labels, values, colors = toolbox.read_csv_column()
    return render_template('chart.html', values=values[1:], labels=labels[1:], set=zip(values[1:], labels[1:], colors[1:]))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)