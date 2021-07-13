import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    with open('destfolder/jsonfolder/books.json', 'r',
              encoding='UTF-8') as file:
        books = json.load(file)
    books_chunked = list(chunked(books, 2))
    rendered_page = template.render(
        books=books_chunked,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    print('Site rebuilt')


on_reload()

server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
