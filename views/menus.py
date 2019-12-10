import pprint

import requests
from flask import Blueprint, render_template

from keys import KAKAO_REST_KEY
from rest_client.read_kakao import KAKAO_BASE_URL
from views.auth import kakao_oauth

menus_blueprint = Blueprint('menus', __name__)
headers = {'Authorization': 'KakaoAK ' + KAKAO_REST_KEY}

@menus_blueprint.route('/main')
def menus_main():
    return 'welcome news {0}'.format("yhhan")

@menus_blueprint.route('/sports')
def menus_sports():
    return 'welcome sports news {0}'.format("yhhan")

@menus_blueprint.route('/books')
def books():
    res1 = requests.get(
        url=KAKAO_BASE_URL + "/v3/search/book?target=title&query=미움받을 용기",
        headers=headers
    )
    if res1.status_code == 200:
        books = res1.json()

        pprint.pprint(books)
        for book in books['documents']:
            print("{0:30s} - {1:20s}".format(book['title'], str(book['authors'])))
    else:
        print("Error {0}".format(res1.status_code))

    return render_template(
        'books.html', books=books['documents'], nav_menu="book", kakao_oauth=kakao_oauth
    )

@menus_blueprint.route('/images')
def images():


    res2 = requests.get(
        url=KAKAO_BASE_URL + "/v2/search/image?query=파이썬",
        headers=headers
    )
    if res2.status_code == 200:
        docs = res2.json()
        pprint.pprint(docs)

        images = []
        for image in docs['documents']:
            images.append(image['image_url'])
    else:
        print("Error {0}".format(res2.status_code))

    return render_template(
        'images.html', images=images, nav_menu="image", kakao_oauth=kakao_oauth
    )
