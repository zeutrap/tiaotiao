# -*- coding: utf-8 -*-


from datetime import datetime
from app.model import db

class FeedRecord(db.Model):
	__tablename__ = 'feeds'
	id = db.Column(db.Integer, primary_key=True) 
	time = db.Column(db.DateTime, default=datetime.now())
	quant = db.Column(db.Integer)

	def __repr__(self):
		return 'At %s eat %d ml' % (str(self.time), self.quant) 

