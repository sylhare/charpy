from flask import Blueprint, render_template

bp = Blueprint('default', __name__, template_folder='templates')


@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('layout/error.html', color="#2B547E", error=404, message_1="THE PAGE", message_2="WAS NOT FOUND"), 404


@bp.app_errorhandler(501)
def page_not_found(error):
    return render_template('layout/error.html', color="#006600", error=501, message_1="FEATURE", message_2="NOT IMPLEMENTED"), 501
