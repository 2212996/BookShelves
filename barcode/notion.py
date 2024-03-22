import requests

NOTION_API_KEY = 'secret_*******************************************'
DATABASE_ID = 'Enter_database_id'

url = 'https://api.notion.com/v1/pages'

headers =  {
    'Notion-Version': '2022-06-28',
    'Authorization': 'Bearer ' + NOTION_API_KEY,
    'Content-Type': 'application/json',
}

json_data = {
    'parent': { 'database_id': DATABASE_ID },
    'properties': {
        '名前': {
            'title': [
                {
                    'text': {
                        'content': '朱帰然'
                    }
                }
            ]
        },
        'タグ': {
            'multi_select': [
                {
                'name': 'Master'
                }
            ]
        },
    },
}

response = requests.post(url, headers=headers, json=json_data)
print(response)