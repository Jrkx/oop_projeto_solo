from classes.collection import Collection
from utils.book_loader import book_loader
from utils.collection_loader import collection_loader

book = book_loader("test_book1")
collection = Collection("collection_test1")
collection.save_collection()
print(collection.books)

collection.add_book(book.title)
collection.save_collection()
print(collection.books)

