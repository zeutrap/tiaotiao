# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from model import db_session
from model.feed import FeedRecord
from datetime import datetime


feed_page = Blueprint('feed_page', __name__)

@feed_page.route('/feed/', methods=['GET', 'POST'])
def feed():
    if request.method == 'POST' and 'key' in request.form:
        record = FeedRecord(time=datetime.now(), quant=int(request.form['key']))
        db_session.add(record)
        db_session.commit()
        return redirect(url_for('.feed'))

    feeds = FeedRecord.query.all()
    return render_template('/feed/feed.html',  feeds = feeds)

@feed_page.route('/feed/delete/<int:feed_id>')
def delete_feed(feed_id):
    db_session.delete(FeedRecord.query.filter_by(id=feed_id).first())
    db_session.commit()
    return redirect(url_for('.feed'))

