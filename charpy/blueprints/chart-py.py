from flask import Blueprint, render_template
import os
from charpy.data_import.io_import import get_csv_data
from charpy import DATA_PATH

bp = Blueprint('charpy', __name__, template_folder='templates')


@bp.route('/')
@bp.route('/charpy')
def chart_demo():
    demo_file_path = os.path.join(DATA_PATH, "pcbanking.csv")
    date, labels, values = get_csv_data(demo_file_path)
    return render_template('chart-py.html', values=values, labels=labels, type='pie')
