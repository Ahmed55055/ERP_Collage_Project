from Application.IApplication import IApplication
from storage.Repository.IStorageRepository import IStorageRepository
from storage.Service.IStorageService import IStorageService
from storage.Repository.StorageRepository import StorageRepository
from storage.Service.StorageService import StorageService
from database.database import SQLiteDatabase
from database.IDatabase import IDatabase
from database.DatabaseInitializer import DatabaseInitializer

class Application(IApplication):
    def __init__(self):
        self.db_name = 'storage.db'
        self.db_config: SQLiteDatabase = None
        self.storage_repo: IStorageRepository = None
        self.storage_service: IStorageService = None
    
    def build(self):
        self.db_config: IDatabase = SQLiteDatabase(self.db_name)
        initializer = DatabaseInitializer(self.db_config)
        initializer.initialize_storage_schema()
        self.storage_repo = StorageRepository(self.db_config)
        self.storage_service = StorageService(self.storage_repo)

    def run(self):
        print("Start application at main screen")