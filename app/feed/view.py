# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.ext.security import login_required
from app.model import db_session
from app.model.feed import FeedRecord
from sqlalchemy import desc
from datetime import datetime
from forms import FeedForm


feed_page = Blueprint('feed_page', __name__)

@feed_page.route('/feed/', methods=['GET', 'POST'])
def feed():
    if request.method == 'POST' and 'key' in request.form:
        record = FeedRecord(time=datetime.now(), quant=int(request.form['key']))
        db_session.add(record)
        db_session.commit()
        return redirect(url_for('.feed'))

    feeds = FeedRecord.query.order_by(desc(FeedRecord.id)).all()
    return render_template('/feed/feed.html',  feeds = feeds)

@feed_page.route('/feed/delete/<int:feed_id>')
@login_required
def delete_feed(feed_id):
    db_session.delete(FeedRecord.query.filter_by(id=feed_id).first())
    db_session.commit()
    flash(u'记录删除成功！')
    return redirect(url_for('.feed'))

@feed_page.route('/feed/edit/<int:feed_id>', methods=("POST", "GET"))
@login_required
def edit_feed(feed_id):
    record = FeedRecord.query.filter(FeedRecord.id == feed_id).first()
    feed_form = FeedForm(request.form, record)
    if request.method == 'POST':
        feed_form.populate_obj(record)
        if 'key' in request.form:
            record.quant = int(request.form['key'])
            db_session.add(record)
            db_session.commit()
            flash(u'记录编辑成功！')
        return redirect(url_for('.feed'))
    else:
        return render_template('feed/edit.html', feed_form=feed_form)
