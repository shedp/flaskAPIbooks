# from data import books
from werkzeug.exceptions import BadRequest
from flask_study.data import data as books
import sys
sys.path.append('..')
from data.data import books

def index(req):
    return [book for book in books], 200

def create(req):
    new_book = req.get_json()
    new_book['id'] = sorted([book['id'] for book in books])[-1] + 1
    books.append(new_book)
    return new_book, 201

def findbyid(id):
    try:
        return next(book for book in books if book['id'] == id)
    except:
        raise BadRequest(f'We don\'t have that book with id {id}')

def show(req, id):
    return findbyid(id), 200

def update(req, id):
    book = findbyid(id)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        book[key] = val
    return book, 200

def destroy(req, id):
    book = findbyid(id)
    books.remove(book)
    return book, 204