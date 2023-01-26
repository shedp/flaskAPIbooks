# from data import books
from werkzeug.exceptions import BadRequest

books = [
    {'id': 1, 'title': 'Death of an Airman', 'author': 'Christopher St John Springg', 'genre': 'crime', 'type': 'softback', 'status': 'read'},
    {'id': 2, 'title': 'Knots & Crosses', 'author': 'Ian Rankin', 'genre': 'crime', 'type': 'softback', 'status': 'read'},
    {'id': 3, 'title': 'Travels In Four Dimensions', 'author': 'Robin Le Poidevin', 'genre': 'science', 'type': 'softback', 'status': 'read'},
    {'id': 4, 'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'genre': 'science', 'type': 'softback', 'status': 'unread'},
    {'id': 5, 'title': 'The Spy Who Came from the Cold', 'author': 'John Le Carre', 'genre': 'crime', 'type': 'softback', 'status': 'read'},
    {'id': 6, 'title': 'A Murder of Quality', 'author': 'John Le Carre', 'genre': 'crime', 'type': 'softback', 'status': 'unread'},
    {'id': 7, 'title': 'The Looking Glass War', 'author': 'John Le Carre', 'genre': 'crime', 'type': 'softback', 'status': 'unread'},
    {'id': 8, 'title': 'Call for the Dead', 'author': 'John Le Carre', 'genre': 'crime', 'type': 'softback', 'status': 'unread'},
    {'id': 9, 'title': 'A Small Town in Germany', 'author': 'John Le Carre', 'genre': 'crime', 'type': 'softback', 'status': 'unread'}
]


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