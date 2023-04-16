from flask import Flask, render_template

from database import db, Book, Genre
import create_bd


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///project.db'
app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def all_books():
    books = Book.query.order_by(Book.added.desc()).limit(15).all()
    return render_template('all_books.html', books=books)


@app.route('/genre/<int:genre_id>')
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template('books_by_genre.html', genre_name=genre.name, books=genre.books)


if __name__ == '__main__':
    app.run()