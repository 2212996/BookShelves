import requests
import json

url = "https://www.googleapis.com/books/v1/volumes?q=isbn:9784873119755"

response = requests.get(url)
contents = json.dumps(
    response.json(), indent=4,
    ensure_ascii=False
)
print(contents)