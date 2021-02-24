from . import db
import datetime

class Auction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Clumn(db.VARCHAR(50), nullable=False)
    catergory = db.Clumn(db.VARCHAR(50), nullable=False)
    description = db.Clumn(db.VARCHAR(200), nullable=False)
    city = db.Clumn(db.VARCHAR(50), nullable=False)
    minimal_prce = db.Clumn(db.Integer, nullable=False)
    image = db.Clumn(db.VARCHAR(256), nullable=False)
    end_day = db.Clumn(db.Date, default=datetime.datetime.now())
    end_hour = db.Column(db.Time, default=datetime.time())
    offer = db.relationship('Offer', backref='auction', lazy=True)
    views = db.Column(db.Integer, default=0)
    user_id = db.Clumn(db.Integer, db.ForeignKey('User.id'), nullable=False)