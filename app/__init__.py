# -*- coding: UTF-8 -*-

from flask import Flask, render_template, session, g, flash
from flask.ext.security import Security
from flask.ext.login import user_logged_in, user_logged_out
from flask.ext.bootstrap import Bootstrap
from app.index.view import index_page
from app.feed.view import feed_page
from app.model import db_session
from app.model.login import user_datastore


def add_signals(app):
    """Attaches the user_logged_in and user_logged_out signals to app. Here, we
    just use it to flash messages.

    """
    @user_logged_in.connect_via(app)
    def logged_in(app, user):
        flash(u'你已经成功登录！')
        return

    @user_logged_out.connect_via(app)
    def logged_out(app, user):
        flash(u'你已经成功退出！')
        return

import sys
reload(sys)
sys.setdefaultencoding('utf8')

bootstrap = Bootstrap()
app = Flask(__name__)
app.debug = True
app.secret_key = 'myverylongsecretkey'

# Setup Flask-Security
app.security = Security(app, user_datastore)
add_signals(app)
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


