import os
from charpy.cruncher import Orc
from charpy import MOCK_PATH
from charpy.chartjs import chart, is_chartjs_type
from flask import Blueprint, abort

bp = Blueprint('chartjs', __name__, template_folder='templates')


@bp.route('/chart/<string:chartype>/', methods=['GET'])
def chart_chartjs(chartype):

    if is_chartjs_type(chartype):
        chart_sdemo = chart.Chart(chartype)
        chart_sdemo.title = "Test chart from template"
        demo = Orc(os.path.join(MOCK_PATH, "pcbanking.csv"))
        chart_sdemo.add_dataset('value', demo.df['value'].tolist())
        chart_sdemo.labels = demo.df['label'].tolist()
        return chart_sdemo.render_flask('view/chartjs_default.html')
    else:
        abort(501)
