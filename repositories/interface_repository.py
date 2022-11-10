import json
import pymongo
import certifi
from bson import ObjectId, DBRef
from typing import Generic, TypeVar, get_args

T = TypeVar('T')


class InterfaceRepository(Generic[T]):
    def __init__(self):
        # Connect to database
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            data_config.get("db-connection"),
            tlsCAFile=ca
        )
        self.data_base = client[data_config.get("db-name")]
        # get generic class
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()

    def load_file_config(self) -> dict:
        with open("config.json", "r") as config:
            data = json.load(config)
        return data

    def find_all(self) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find({}):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def find_by_id(self, id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        document = current_collection.find_one({'_id': _id})
        document = self.get_values_db_ref(document)
        if document:
            document['_id'] = document['_id'].__str__()
        else:
            # Document not fund
            document = {}
        return document

    def save(self, item: T) -> T:
        current_collection = self.data_base[self.collection]
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            # Update
            id_ = item._id
            _id = ObjectId(id_)
            delattr(item, '_id')
            item = item.__dict__
            update_item = {'$set': item}
            current_collection.update_one({'_id': _id}, update_item)
        else:
            # Insert
            _id = current_collection.insert_one(item.__dict__)
            id_ = _id.inserted_id.__str__()
        return self.find_by_id(id_)

    def update(self, id_: str, item: T) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        item = item.__dict__
        update_item = {"$set": item}
        document = current_collection.update_one({'_id': _id}, update_item)
        return {"update_count": document.matched_count}

    def delete(self, id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        result = current_collection.delete_one({"_id": _id})
        return {"delete_count": result.deleted_count}

    def query(self, query: dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def query_aggregation(self, query:dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.aggregate(query):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    # Mongo to Python
    def get_values_db_ref(self, document: dict) -> dict:
        for key in document.keys():
            if isinstance(document.get(key), DBRef):
                collection_ref = self.data_base[document.get(key).collection]
                _id = ObjectId(document.get(key).id)
                document_ref = collection_ref.find({'_id': _id)
                document_ref['_id'] = document_ref['_id'].__str__()
                document[key] = document_ref


    def get_values_db_ref_from_list(self):
        pass

    def transform_object_ids(self):
        pass

    def format_list(self):
        pass

    # Python to Mongo
    def transform_refs(self):
        pass

    def object_to_db_ref(self):
        pass
