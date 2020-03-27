from flask import abort, current_app, redirect, render_template, request

from database import db
from models import UrlAssociation
from services import generate_short_url


def index():
    if request.method == 'GET':
        return render_template('request.html')

    fullurl = request.form['url']
    shorturl = generate_short_url(fullurl, current_app.config['TINYURL_URLLENGTH'])

    url_association = db.session.query(UrlAssociation).filter_by(shorturl=shorturl).first()
    if url_association is None:
        url_association = UrlAssociation()
        url_association.fullurl = fullurl
        url_association.shorturl = shorturl
        db.session.add(url_association)
        db.session.commit()
    else:
        url_association.fullurl = fullurl
        db.session.commit()

    return render_template('response.html', url=url_association.shorturl)


def shorturl(url):
    url_association = db.session.query(UrlAssociation).filter_by(shorturl=url).first()
    if url_association is None:
        abort(404)
    return redirect(url_association.fullurl)
