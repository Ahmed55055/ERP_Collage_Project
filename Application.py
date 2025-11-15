from IApplication import IApplication
from storage.IStorageRepository import IStorageRepository
from storage.IStorageService import IStorageService
from storage.StorageRepository import StorageRepository
from storage.StorageService import StorageService
from database.config import DatabaseConfig

class Application(IApplication):
    def __init__(self):
        self.db_name = 'storage.db'
        self.db_config: DatabaseConfig = None
        self.storage_repo: IStorageRepository = None
        self.storage_service: IStorageService = None
    
    def build(self):
        self.db_config = DatabaseConfig(self.db_name)
        self.storage_repo = StorageRepository(self.db_config)
        self.storage_service = StorageService(self.storage_repo)

    def run(self):
        print("Start application at main screen")