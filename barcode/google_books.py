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

    if data["totalItems"] > 0:
        volume_info = data["items"][0]["volumeInfo"]
        title = volume_info["title"]
        published_date = volume_info["publishedDate"]
        thumbnail_link = volume_info["imageLinks"]["thumbnail"]

        if verbose:
            print("\nISBN: {}".format(isbn))
            print("\t- " + title)
            print("\t- " + published_date)
            print("\t- Thumbnail: {}".format(thumbnail_link))

    else:
        title, published_date, thumbnail_link = None, None, None
        if verbose:
            raise ValueError("No book was found for ISBN '{}'".format(isbn))
    
    return title, published_date, thumbnail_link

def cui(isbn: int):
    """Ask the user if to add a book into Notion database."""
    # acquire book information
    title, published_date, thumbnail_link = search_isbn(isbn, verbose=True)

    # show simple dialogue
    text = input("Are you sure to upload the book to Notion? [y/n]: ")
    match text:
        case "y":
            add_book_info(title, published_date, thumbnail_link)
            print("Done!")
        case "n":
            print("Okay, then.")
        case _:
            print("Invarid option was chosen.")


if __name__ == "__main__":
    
    # add a book into Notion database
    isbn = 9784537214192    # "The Wine"
    cui(isbn)