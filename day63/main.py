from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.secret_key = 'gfhdf'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

db.init_app(app)
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column( Float, nullable=False)



@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.id.desc())).scalars()
    return render_template('index.html', books = all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = Books(
            title = request.form['title'],
            author = request.form['author'],
            rating = float(request.form['rating']),
        )
        db.session.add(book)
        db.session.commit()
        flash('Book Added Successfully', 'success')
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    book = db.get_or_404(Books, id)
    db.session.delete(book)
    db.session.commit()
    flash('Book Deleted Successfully', 'success')
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

