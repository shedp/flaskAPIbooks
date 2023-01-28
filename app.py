from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
# ...
from flask_cors import CORS
from werkzeug import exceptions
# from flask_navigation import Navigation

from controllers import authors, books


app = Flask(__name__)
CORS(app)


@app.route("/")
def welcome():
    return render_template('home.html')

@app.route("/books", methods=['GET','POST'])
def books_index():
    fns = {
        'GET': books.index,
        'POST': books.create
    }
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')
        type = request.form.get('type')
        status = request.form.get('status')
        data = {'id': 0, 'title': title, 'author': author, 'genre':genre, 'type':type, 'status':status}
        resp, code = fns[request.method](data)
    else: 
        resp, code = fns[request.method](request)
    return render_template('books.html', books=resp)

@app.route('/books/<int:book_id>', methods=['GET', 'PUT','DELETE'])
def books_show(book_id):
    fns = {
        'GET': books.show,
        'PUT': books.update,
        'DELETE': books.destroy
    }
    resp, code = fns[request.method](request, book_id)
    if request.method == 'PUT':
        req = {'id':request.form['id']}
        print(req)
        return redirect(url_for('books_show', book_id=book_id))
    return render_template('book.html', book=resp)

@app.route('/books/<int:book_id>/edit', methods=['GET'])
def book_edit(book_id):
    fns = {
        'GET': books.show,
    }
    resp, code = fns[request.method](request, book_id)
    return render_template('edit_book.html', book=resp)

@app.route('/books/new', methods=['GET','POST'])
def book_new():
    fns = {
        'GET': books.index,
        'POST': books.create,
    }
    resp, code = fns[request.method](request)
    return render_template('new_book.html', book=resp)


@app.route('/authors', methods=['GET','POST'])
def authors_index():
    fns = {
        'GET': authors.index,
        'PATCH': authors.create
    }
    resp, code = fns[request.method](request)
    return render_template('authors.html', authors=resp)

@app.route('/authors/<int:author_id>', methods=['GET'])
def author_show(author_id):
    fns = {
        'GET': authors.show,
    }
    resp, code = fns[request.method](request, author_id)
    return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)