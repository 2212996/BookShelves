import requests
from notion import add_book_info

def search_isbn(isbn: int, verbose=False):
    """
    Function to search ISBN value in Google Books.

    Parameters
    ----------
    isbn: int
    verbose: bool

    Returns
    -------
    title, published_date, thumbnail_link: str
        Information about the book.
    """
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:{}".format(isbn)

    response = requests.get(url)
    data = response.json()

    volume_info = data["items"][0]["volumeInfo"]
    title = volume_info["title"]
    published_date = volume_info["publishedDate"]
    thumbnail_link = volume_info["imageLinks"]["thumbnail"]

    if verbose:
        print(title)
        print(published_date)
        print(thumbnail_link)
    
    return title, published_date, thumbnail_link


if __name__ == "__main__":
    
    # search book
    isbn = 9784537214192    # "The Wine"
    title, published_date, thumbnail_link = search_isbn(isbn, verbose=True)

    # add to Notion database (option)
    text = input("Are you sure to upload the book to Notion? [y/n]: ")
    match text:
        case "y":
            add_book_info(title, published_date, thumbnail_link)
            print("Done!")
        case "n":
            print("Okay, then.")
        case _:
            print("Invarid option was chosen.")