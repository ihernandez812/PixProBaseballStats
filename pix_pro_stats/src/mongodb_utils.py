from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import certifi

class Database:

    def __init__(self, ip: str=None, port: str=None, uri: str=None) -> None:
        self.ip = ip
        self.port = port
        self.uri = uri
        self.connection = None
        self.database = None

    def create_connection(self) -> MongoClient:
        if not self.uri:
            self.connection = MongoClient(self.ip, self.port)
        else:
            self.connection = MongoClient(self.uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    
    def set_database(self, database_name: str) -> None:
        if not self.connection:
            raise ValueError('Connection is not set')
        self.database = self.connection[database_name]
    
    def ping_connection(self) -> None:
        if self.connection is None:
            raise ValueError('Connection is not set')
        self.connection.admin.command('ping')

    def get_collection(self, collection_name: str) -> Collection:
        if self.database is None:
            raise ValueError('Database is not set')
        return self.database[collection_name]

    def close_connection(self) -> None:
        self.connection.close()
        
    def convert_to_object_id(self, document_id: str) -> ObjectId:
        return ObjectId(document_id)