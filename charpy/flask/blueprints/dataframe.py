from flask import Blueprint, render_template
import os
from charpy.cruncher import Orc
from charpy import MOCK_PATH

bp = Blueprint('dataframe', __name__, template_folder='templates')


@bp.route('/dataframe')
def chart_demo():
    demo = Orc(os.path.join(MOCK_PATH, "pcbanking.csv"))
    demo.format_column_list('label')
    demo.create_from_list_column('label')
    demo.create_from_date_column('date', formatting='day')
    demo.create_from_date_column('date', formatting='month')
    demo.create_from_date_column('date', formatting='year')

    collapse_border = "<style>.dataframe {font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%;}"
    header = ".dataframe th {padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #336699;color: white;}"
    padding_border = ".dataframe td, .dataframe th {border: 1px solid #ddd;padding: 8px;}"
    hover = ".dataframe tr td:hover {background-color: #ddd;}"
    highlight = ".dataframe tbody tr:nth-child(even) {background-color: #f8f8f8;}</style>"
    return collapse_border + header + hover + padding_border + highlight + demo.df.to_html()
