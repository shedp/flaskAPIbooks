from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from werkzeug import exceptions
from controllers import books
from controllers import authors


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
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/books/<int:book_id>', methods=['GET', 'PATCH','DELETE'])
def books_show(book_id):
    fns = {
        'GET': books.show,
        'PATCH': books.update,
        'DELETE': books.destroy
    }
    resp, code = fns[request.method](request, book_id)
    return jsonify(resp), code

@app.route('/authors', methods=['GET','POST'])
def authors_index():
    fns = {
        'GET': authors.index,
        'PATCH': authors.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/authors/<int:author_id>', methods=['GET', 'PATCH','DELETE'])
def author_show(author_id):
    fns = {
        'GET': authors.show,
        'PATCH': authors.update,
        'DELETE': authors.destroy
    }
    resp, code = fns[request.method](request, author_id)
    return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)