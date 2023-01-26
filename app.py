from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions

app = FLASK(__name__)
CORS(app)

@app.route("/")
def welcome():
    return "Hello World", 200

@app.route("/books", method=['GET','POST'])
def books_index():
    fns = {
        'GET': books.index,
        'POST': books.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('books/<int:book_id>', methods=['GET', 'PATCH','DELETE'])
def books_show(book_id):
    fns = {
        'GET': books.show,
        'PATCH': books.update,
        'DELETE': books.destroy
    }
    resp, code = fns[request.method](request, book_id)
    return jsonify(resp), code



if __name__ == "__main__":
    app.run(debug=True)