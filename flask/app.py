from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first = db.Column(db.String(80), unique=False, nullable=False)
    last = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    isActive = db.Column(db.Boolean(120), unique=False, nullable=False)
    siteId = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=False)

    site = db.relationship('Site', backref=db.backref('user', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.country


@app.route("/")
def hello():
    return "Hello World!"
