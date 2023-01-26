# from data import authors
from werkzeug.exceptions import BadRequest

authors = [
    {'id': 1, 'author': 'Christopher St John Springg', 'no_of_books': 1},
    {'id': 2, 'author': 'Ian Rankin', 'no_of_books': 1},
    {'id': 3, 'author': 'Robin Le Poidevin', 'no_of_books': 1},
    {'id': 4, 'author': 'Stephen Hawking', 'no_of_books': 1},
    {'id': 5, 'author': 'John Le Carre', 'no_of_books': 5}
]

def index(req):
    return [author for author in authors], 200

def create(req):
    new_author = req.get_json()
    new_author['id'] = sorted([author['id'] for author in authors])[-1] + 1
    authors.append(new_author)
    return new_author, 201

def findbyid(id):
    try:
        return next(author for author in authors if author['id'] == id)
    except:
        raise BadRequest(f'We don\'t have that author with id {id}')

def show(req, id):
    return findbyid(id), 200

def update(req, id):
    author = findbyid(id)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        author[key] = val
    return author, 200

def destroy(req, id):
    author = findbyid(id)
    authors.remove(author)
    return author, 204