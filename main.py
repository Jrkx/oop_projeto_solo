import os
from classes.book import Book
from classes.collection import Collection
from utils.book_loader import book_loader
from utils.collection_loader import collection_loader

def main():
    print("Welcome to personal book collection manager\n")
    collection_name = input("please, enter the name of your colection: ")
    
    path = f"{os.path.dirname(__file__)}/data/collections/{collection_name}.json"

    if os.path.isfile(path):
        collection = collection_loader(collection_name)

    else:
        collection = Collection(name=collection_name)

    while True:
        print("\n1. view collection")
        print("2. add book to collection")
        print("3. remove book from the collection")
        print("4. exit\n")

        option = input("please, choose one option: ")

        if option == "1":
            for book in collection.books:
                print(f"- {book}")

        elif option == "2":
            title = input("please, enter the title of the book: ")
            message = collection.add_book(title)
            print(message)

        elif option == "3":
            title = input("please, enter the title of the book: ")
            message = collection.remove_book(title)
            print(message)

        elif option == "4":
            print("\ngoodbye")
            break

        else:
            print(f"{option} not a valid option, please try again.")
if __name__ == "__main__":
    main()
