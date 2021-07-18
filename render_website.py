import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked


def on_reload():
    with open('static/jsonfolder/books.json', 'r',
              encoding='UTF-8') as file:
        books = json.load(file)
    pages = list(chunked(books, 10))
    pages_amount = len(pages)
    os.makedirs('pages', exist_ok=True)
    for number, page in enumerate(pages, 1):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('template.html')

        books_chunked = list(chunked(page, 2))
        rendered_page = template.render(
            books=books_chunked,
            pages_amount=pages_amount,
            previous_page=number - 1,
            current_page=number,
            next_page=number + 1

        )

        with open(f'pages/index{number}.html', 'w',
                  encoding="utf8") as file:
            file.write(rendered_page)
        # print(f'Page {number} rebuilt')


on_reload()

server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
