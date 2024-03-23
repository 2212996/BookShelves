# Use Notion API to create object in database.
import requests
import json

NOTION_API_KEY = 'secret_IyEtg4cZu4DWoxGc0OCDX22QkOIXDxAdnEUH8CCCZz5'
DATABASE_ID = '068ea96919534bcf9adba807c9f75833'    # 書籍一覧

def upload_image(image_path):

    # 画像をアップロード
    image_url = ''
    with open(image_path, 'rb') as file:
        image_data = file.read()
        headers = {
            'Authorization': f'Bearer {NOTION_API_KEY}',
            'Content-Type': 'image/jpg',  # 画像ファイルの形式に合わせて変更
        }
        response = requests.post('https://api.notion.com/v1/files', headers=headers, data=image_data)
        print(response.json())
        # image_url = response.json()['uri']

    return image_url

def get_page_ids(database_id):
    """Function to get information of current pages in database"""
    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    headers =  {
        'Notion-Version': '2022-06-28',
        'Authorization': 'Bearer ' + NOTION_API_KEY,
        'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers)
    data = response.json()
    with open("barcode/current_books.json", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_book_info(title, published_date, thumbnail_link):

    url = 'https://api.notion.com/v1/pages'
    headers =  {
        'Notion-Version': '2022-06-28',
        'Authorization': 'Bearer ' + NOTION_API_KEY,
        'Content-Type': 'application/json',
    }

    # upload thumnail
    img_url = "https://m.media-amazon.com/images/I/71uAya7R8YL._AC_UF1000,1000_QL80_.jpg"

    json_data = {
        'parent': {'database_id': DATABASE_ID},
        'properties': {
            '名前': {
                'title': [
                    {'text': {'content': title}}
                ]
            },
            "出版年": {
                "rich_text": [
                    {
                        "text": {
                            "content": published_date
                        }
                    }
                ]
            },
        },
    }

    response = requests.post(url, headers=headers, json=json_data)
    print(response)

if __name__ == "__main__":
    # add_book_info(
    #     title="卒業論文", published_date="2024-1-31",
    #     thumbnail_link="https://m.media-amazon.com/images/I/71llCWZhNfL._AC_UF1000,1000_QL80_.jpg"
    # )
    get_page_ids(DATABASE_ID)