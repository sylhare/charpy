from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/pages/<page>')
def show(page):
    try:
        # return render_template('pages/%s.html' % page) # To open the template corresponding of the url
        return "The page name is: " + page
    except TemplateNotFound:
        abort(404)


@simple_page.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
