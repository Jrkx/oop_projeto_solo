from .book import Book
import os
import json
from utils.collection_encoder import collection_encoder
class Collection():
    def __init__(self, name: str = None, books: list = None):
        self.__name = name
        self.__books = books if books is not None else []

    @property
    def name(self) -> str:
        """get the collectio name."""
        return self.__name
    
    @property
    def books(self) -> list:
        """get the books in the collection."""
        return self.__books

    def set_name(self, name: str) -> None:
        """set the name of a collection or change it if already set"""
        if not isinstance(name, str):
            raise ValueError("name must be a string.")
        self.__name = name
        self.save_collection()

    def add_book(self, title: str) -> None:
        """add a book to the list of books in the collection."""
        if title in self.books:
            return f"book {title} already in the collection."

        if not isinstance(title, str):
            raise ValueError("title must be a string.")
        self.__books.append(title)
        self.save_collection()
        return f"book '{title}' add sucessfully"

    def remove_book(self, title: str) -> None:
        """remove a book from the list of books in the collection."""
        if title not in self.books:
            return f"book '{title}' not in the in the collection"

        if not isinstance(title, str):
            raise ValueError("title must be a string.")
        self.__books.remove(title)
        self.save_collection()
        return f"book '{title}' removed sucessfully"
    def save_collection(self):
        """save the changes in a collection or add a new collection in the data base."""
        path_to_save = f"{os.path.dirname(__file__)}/../data/collections/{self.name}.json"
        collection_to_save = self
        try:
            with open(path_to_save, 'w') as file:
                json.dump(collection_to_save, file, default=collection_encoder, indent=4)
        except FileNotFoundError:
            return f"File {path_for_save} not found"

    
    
    
    
    
    
    



