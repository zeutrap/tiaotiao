# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, g
from flask.ext.bootstrap import Bootstrap
from app.index.view import index_page
from app.feed.view import feed_page
from app.model import db_session


bootstrap = Bootstrap()
app = Flask(__name__)
app.debug = True
app.secret_key = 'myverylongsecretkey'
bootstrap.init_app(app)
# register blueprint
app.register_blueprint(index_page)
app.register_blueprint(feed_page)


# error handler
@app.errorhandler(404)
def page_not_found(error):
	"""
	404 page not found
	"""
	return render_template('404.html'), 404


@app.before_request
def before_request():
	"""
	before request
	"""
	if 'is_admin' in session:
		g.is_admin = 1
	else:
		g.is_admin = None


@app.teardown_request
def shutdown_session(exception=None):
	"""
	teardown request
	"""
	db_session.rollback()
	db_session.close()
