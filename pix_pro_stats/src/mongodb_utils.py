from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import certifi

class Database:

    def __init__(self, ip=None, port=None, uri=None):
        self.ip = ip
        self.port = port
        self.uri = uri
        self.connection = None
        self.database = None

    def create_connection(self):
        if not self.uri:
            self.connection = MongoClient(self.ip, self.port)
        else:
            self.connection = MongoClient(self.uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    
    def set_database(self, database_name):
        if not self.connection:
            raise ValueError('Connection is not set')
        self.database = self.connection[database_name]
    
    def ping_connection(self):
        if self.connection is None:
            raise ValueError('Connection is not set')
        self.connection.admin.command('ping')

    def get_collection(self, collection_name):
        if self.database is None:
            raise ValueError('Database is not set')
        return self.database[collection_name]

    def close_connection(self):
        self.connection.close()
    def convert_to_object_id(self, document_id):
        return ObjectId(document_id)