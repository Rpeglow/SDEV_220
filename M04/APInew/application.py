"""
Reed Peglow
SDEV 220
M04 Lab - Case Study: Python APIs
"""
# import and start app
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
#configure the database storage location 
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#class to be called to and setup of SQL table *note not all books are published*
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120)nullable=True)

#reads itself and returns identities
def __repr__(self):
    return f"{self.id} - {self.book_name} - {self.author} - {self.publisher}"

#welcome screen
@app.route('/')
def index():
    return "Welcome to the Book page:"

#sorted to subfolder books, function iterates through whole list and returns a list 
@app.route('/books')
def get_book():
    books = Book.query.all()

    output = []
    for book in books:
        book_data ={'name': book.book_name, 'author':book.author, 'publisher': book.publisher}

        output.append(book_data)

    return {"books":output}

#ablity to search books by ID number
@app.route("/books/<id>")
def get_book(id):
    book= Book.query.get_or_404(id)
    return {"name":book.name, "author":book.author, 'publisher': book.publisher}

#function to POST/add book to books subfolder
@app.route('/books', methods=['POSt'])
def add_book():
    book = Book(name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id':book.id}


#function to DELETE books by ID number *error checking if no books match ID
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error":"not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message":"Deleted"}