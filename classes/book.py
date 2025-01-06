import os
import json
from utils.book_encoder import book_encoder
class Book:
    def __init__(self, title: str = None):
        self.__title = title

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        if not isinstance(title, str):
            raise ValueError("title must be a string.")
        self.__title = title

    def serialize_book(self):
        path_to_book = f"{os.path.dirname(__file__)}/../data/books/{self.title}.json"
        book_to_serialize = self
        try:
            with open(path_to_book, 'w') as file:
                json.dump(book_to_serialize, file, default=book_encoder, indent=4)
        except FileNotFoundError:
            return f"file {path_to_book} not found"
                
