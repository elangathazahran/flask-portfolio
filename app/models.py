from app import db


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(100))
    live_link = db.Column(db.String(200))
    github_link = db.Column(db.String(200))
