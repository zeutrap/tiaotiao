# -*- coding: utf-8 -*-
from flask_wtf.form import Form
from wtforms import TextAreaField, IntegerField, SelectField, StringField, DateTimeField
from wtforms.validators import Length, DataRequired


class FeedForm(Form):
	"""
	edit form
	"""
	id = IntegerField('id', validators=[
		DataRequired(u'id不能为空')])
	time = DateTimeField(u'喂奶时间')
	quant = IntegerField('quant')


