from flask import Flask
from flask import render_template
from charpy import toolbox
from charpy.blueprints.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
# app.register_blueprint(simple_page, url_prefix='/pages') # to register blueprint at different location


@app.route("/")
def chart_demo():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC", "#BCAFED"]
    return render_template('chart.html', values=values, labels=labels, set=zip(values, labels, colors))


@app.route("/chart")
def chart_file():
    labels, values, colors = toolbox.get_demo_data()
    return render_template('chart.html', values=values, labels=labels, set=zip(values, labels, colors))


@app.route("/hello/<string:name>/")
def hello(name):
    return "hello " + name + "!"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)