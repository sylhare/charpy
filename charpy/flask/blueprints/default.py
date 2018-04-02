from flask import Blueprint, render_template

bp = Blueprint('default', __name__, template_folder='templates')


@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=404, message_1="THE PAGE", message_2="WAS NOT FOUND"), 404
