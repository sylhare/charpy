from flask import Blueprint, abort, Response, render_template
import os
from charpy.cruncher import Orc
from charpy import MOCK_PATH

bp = Blueprint('dataframe', __name__, template_folder='templates')


@bp.route('/v1/dataframe')
def chart_demo():
    demo = Orc(os.path.join(MOCK_PATH, "pcbanking.csv"))
    demo.format_column_list('label')
    demo.create_from_list_column('label')
    demo.create_from_date_column('date', formatting='day')
    demo.create_from_date_column('date', formatting='month')
    demo.create_from_date_column('date', formatting='year')

    return render_template('dataframe.html', body=demo.df.to_html())


@bp.route("/v1/dataframe/<string:column>/", methods = ['GET'])
def get_dataframe_data(column):
    demo = Orc(os.path.join(MOCK_PATH, "pcbanking.csv"))
    try:
        response = Response(
            response=demo.get_json_data(column),
            status=200,
            mimetype='application/json'
        )
        return response
    except KeyError:
        abort(404)
