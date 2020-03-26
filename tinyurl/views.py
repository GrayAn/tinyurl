from flask import abort, current_app, redirect, render_template, request

from database import db
from models import UrlAssociation
from services import generate_short_url


def index():
    if request.method == 'GET':
        return render_template('request.html')
    url_length = current_app.config['TINYURL_URLLENGTH']
    url_association = UrlAssociation()
    url_association.fullurl = request.form['url']
    url_association.shorturl = generate_short_url(request.form['url'], url_length)
    db.session.add(url_association)
    db.session.commit()
    return render_template('response.html', url=url_association.shorturl)


def shorturl(url):
    url_association = db.session.query(UrlAssociation). \
            filter_by(shorturl=url).first()
    if url_association is None:
        abort(404)
    return redirect(url_association.fullurl)
