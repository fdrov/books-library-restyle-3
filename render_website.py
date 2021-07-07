from http.server import HTTPServer, SimpleHTTPRequestHandler

import json

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


with open('destfolder/jsonfolder/books.json', 'r', encoding='UTF-8') as file:
    books = json.load(file)

print(books[0])
rendered_page = template.render(
    books=books,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()