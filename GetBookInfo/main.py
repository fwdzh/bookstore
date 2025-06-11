

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from bs4 import BeautifulSoup
import sys

from store.models import Book

# sys.stdout = open('BookInfo.txt', 'w', encoding='utf-8')

# st = set()
for page in range(1, 6):
    with open(f'page{page}.txt', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.select('.all-img-list.cf li'):
        title = item.select_one('h2').text
        author = item.select_one('.name').text
        book_type = item.select_one('[data-eid=qd_B60]').text
        img_url = 'https:' + item.select_one('img')['src']
        intro = item.select_one('.intro').text
        try:
            book = Book(title=title, author=author, book_type=book_type, img_url=img_url, intro=intro)
            # print(book)
            book.save()
        except Exception as e:
            print(f'saveError: {e}')