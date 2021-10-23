from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/librarycatalog'
app.debug = True
db = SQLAlchemy(app)
class books(db.Model):
    __tablename__ = 'books'
    bookTitle = db.Column(db.String, primary_key = True)
    bookText = db.Column(db.String, nullable = False)
    likes = db.Column(db.Integer, nullable = False)
    def __init__(self, bookTitle, BookText, likes):
        self.bookTitle = bookTitle
        self.bookTitle = BookText
        self.likes = likes
@app.route("/test", methods=['GET'])
def test():
    return {
        'test': 'test1'
    }
