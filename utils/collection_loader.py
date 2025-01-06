import os
import json
from classes.collection import Collection
def collection_loader(collection_name):
    path_to_load = f"{os.path.dirname(__file__)}/../data/collections/{collection_name}.json"
        
    try:
        with open(path_to_load, 'r') as file:
            data = json.load(file)
        collection_to_load = Collection(**data)
        return collection_to_load
    except FileNotFoundError:
        return f"file {path_to_load} not found"


