from flask import Blueprint, abort, current_app, redirect, render_template, request
from werkzeug.security import gen_salt

from database import db
from models import UrlAssociation

views_blueprint = Blueprint(__name__, __name__)


@views_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('request.html')
    url_length = current_app.config['TINYURL_URLLENGTH']
    url_association = UrlAssociation()
    url_association.fullurl = request.form['url']
    # TODO: Checking for short URL collision
    # TODO: Deterministic algorithm of short URL generation to minimize collisions
    url_association.shorturl = gen_salt(url_length)
    db.session.add(url_association)
    db.session.commit()
    return render_template('response.html', url=url_association.shorturl)


@views_blueprint.route('/<url>')
def shorturl(url):
    url_association = db.session.query(UrlAssociation). \
            filter_by(shorturl=url).first()
    if url_association is None:
        abort(404)
    return redirect(url_association.fullurl)