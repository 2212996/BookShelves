import requests
import json
from notion import add_book_info

isbn = 9784296114788
url = "https://www.googleapis.com/books/v1/volumes?q=isbn:{}".format(isbn)

response = requests.get(url)
data = response.json()
contents = json.dumps(data, indent=4, ensure_ascii=False)

volume_info = data["items"][0]["volumeInfo"]
title = volume_info["title"]
published_date = volume_info["publishedDate"]
thumnbail_link = volume_info["imageLinks"]["thumbnail"]

print(title)
print(published_date)
print(thumnbail_link)

text = input("Sure to upload following book to Notion? [y/n]: ")
match text:
    case "y":
        add_book_info(title, published_date, thumnbail_link)
        print("Done!")
    case "n":
        print("Okay, then.")
    case _:
        print("Invarid option was chosen.")