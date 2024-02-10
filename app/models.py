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


class MLGameSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(100), nullable=False)
    original_story = db.Column(db.Text, nullable=False)
    final_story = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user_inputs = db.relationship('MLUserInput', backref='ml_game_session', lazy='dynamic')

    def __repr__(self):
        return f'<MLGameSession {self.theme} at {self.timestamp}>'

class MLUserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Correct the ForeignKey reference to match the MLGameSession table name
    session_id = db.Column(db.Integer, db.ForeignKey('ml_game_session.id'), nullable=False)
    placeholder_type = db.Column(db.String(50), nullable=False)
    original_word = db.Column(db.String(100), nullable=True)
    user_input = db.Column(db.String(100), nullable=False)
    position = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<MLUserInput {self.placeholder_type}: {self.user_input} for session {self.session_id}>'
