from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, unique=True)
    author = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Book {self.title}>'