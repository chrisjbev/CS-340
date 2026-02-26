from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """
    CRUD operations for the aac.animals collection
    """

    def __init__(self, username, password, host='localhost', port=27017):
        """
        Initialize MongoDB connection.
        """
        try:
            self.client = MongoClient(
                f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
            )
            self.database = self.client['aac']
            self.collection = self.database['animals']
        except PyMongoError as e:
            print("Connection error:", e)

    def create(self, data):
        """
        Inserts a document into the collection.
        Returns True if successful, False otherwise.
        """
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError as e:
                print("Insert failed:", e)
                return False
        else:
            return False

    def read(self, query):
        """
        Queries documents from the collection.
        Returns a list of results or an empty list.
        """
        results = []
        try:
            cursor = self.collection.find(query)
            for document in cursor:
                results.append(document)
        except PyMongoError as e:
            print("Read failed:", e)
        return results

    def update(self, query, new_values):
        """
        Updates document(s) in the collection.
        Returns number of documents modified.
        """
        try:
            result = self.collection.update_many(query, new_values)
            return result.modified_count
        except PyMongoError as e:
            print("Update failed:", e)
            return 0

    def delete(self, query):
        """
        Deletes document(s) from the collection.
        Returns number of documents deleted.
        """
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print("Delete failed:", e)
            return 0
