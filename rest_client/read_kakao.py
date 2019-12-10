import requests
from keys import KAKAO_REST_KEY
import pprint

KAKAO_BASE_URL = "https://dapi.kakao.com"

if __name__ == "__main__":
    headers = {'Authorization': 'KakaoAK ' + KAKAO_REST_KEY}

    res1 = requests.get(
        url=KAKAO_BASE_URL + "/v3/search/book?target=title&query=미움받을 용기",
        headers=headers
    )
    if res1.status_code == 200:
        books = res1.json()
        #pprint.pprint(books['documents'])
        for book in books['documents']:
            print("{0:30s} - {1:20s}".format(book['title'], str(book['authors'])))
    else:
        print("Error {0}".format(res1.status_code))


    res2 = requests.get(
        url=KAKAO_BASE_URL + "/v2/search/image?query=설현",
        headers=headers
    )
    if res2.status_code == 200:
        docs = res2.json()
        #pprint.pprint(docs)

        images = []
        for image in docs['documents']:
            images.append(image['image_url'])

        print(images)
    else:
        print("Error {0}".format(res2.status_code))