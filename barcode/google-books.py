import os
from googleapiclient.discovery import build

def get_book_info(isbn):
    # Google Books APIを利用して情報を取得
    service = build('books', 'v1')
    request = service.volumes().list(q=f"isbn:{isbn}")
    response = request.execute()

    # 情報が取得できなかった場合
    if 'items' not in response:
        print("No information found for this ISBN.")
        return

    # 最初のアイテムの情報を返す
    item = response['items'][0]
    volume_info = item['volumeInfo']

    title = volume_info.get('title', 'Title not available')
    authors = volume_info.get('authors', ['Author not available'])
    publisher = volume_info.get('publisher', 'Publisher not available')
    published_date = volume_info.get('publishedDate', 'Published date not available')
    description = volume_info.get('description', 'Description not available')

    print("Title:", title)
    print("Authors:", ", ".join(authors))
    print("Publisher:", publisher)
    print("Published Date:", published_date)
    print("Description:", description)

if __name__ == "__main__":
    os.environ["CLOUDSDK_PYTHON "] = "/Users/naoki/anaconda3/envs/app-books/bin/python"
    # isbn = input("Enter ISBN-13: ")
    isbn = 9784873119755
    get_book_info(isbn)