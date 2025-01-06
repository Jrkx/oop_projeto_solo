import os
import json
from classes.book import Book
def book_loader(book_title):
    path_to_load = f"{os.path.dirname(__file__)}/../data/books/{book_title}.json"
        
    try:
        with open(path_to_load, 'r') as file:
            data = json.load(file)
        book_to_load = Book(**data)
        return book_to_load
    except FileNotFoundError:
        return f"file {path_to_load} not found"
