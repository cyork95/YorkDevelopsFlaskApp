from datetime import datetime

from app import db


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    summary = db.Column(db.String(255))

    def __repr__(self):
        return f'<BlogPost {self.title}>'
