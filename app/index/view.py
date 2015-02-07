# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for


index_page = Blueprint('index_page', __name__)


@index_page.before_request
def before_request():
    """
    before
    :return:
    """
    pass


@index_page.route('/')
@index_page.route('/<int:page>')
def index(page=1):
    """
    index page
    :param page:
    :return:
    """
    return redirect(url_for('feed_page.feed'))


@index_page.teardown_request
def teardown_request(exception):
    """
    teardown
    :param exception:
    :return:
    """
    pass
