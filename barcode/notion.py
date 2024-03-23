# Use Notion API to create object in database.
import requests
import json
import os

DATABASE_ID = "068ea96919534bcf9adba807c9f75833"    # 書籍一覧

def get_api_key(name: str) -> str:
    """
    Function to get API key from environment variable.

    Parameters
    ----------
    name: str
        Name of environment variable.

    Return
    ------
    api_key: str
    """
    api_key = os.environ.get(name)
    if api_key:
        return api_key
    else:
        api_key = input("Enter Notion API key: ")
        os.environ[name] = api_key
        return api_key

def get_page_ids(database_id):
    """Function to get information of current pages in database"""
    NOTION_API_KEY = get_api_key("NOTION_API_KEY")

    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    headers =  {
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer " + NOTION_API_KEY,
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers)
    data = response.json()
    with open("barcode/current_books.json", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_book_info(title, published_date, thumbnail_link):
    """Function to add book information to given database."""

    NOTION_API_KEY = get_api_key("NOTION_API_KEY")

    url = "https://api.notion.com/v1/pages"
    headers =  {
        "Notion-Version": "2022-06-28",
        "Authorization": "Bearer " + NOTION_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "cover": {
            "type": "external",
            "external": {
                "url": thumbnail_link
            }
        },
        "properties": {
            "名前": {
                "title": [
                    {"text": {"content": title}}
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

    response = requests.post(url, headers=headers, json=payload)
    print(response)

if __name__ == "__main__":
    
    add_book_info(
        title="卒業論文", published_date="2024-1-31",
        thumbnail_link="https://m.media-amazon.com/images/I/71llCWZhNfL._AC_UF1000,1000_QL80_.jpg"
    )

    get_page_ids(DATABASE_ID)