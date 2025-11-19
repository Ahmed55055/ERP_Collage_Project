from .IStorageService import IStorageService
from ..Repository.IStorageRepository import IStorageRepository
from ..dto import ItemDto


class StorageService(IStorageService):

    def __init__(self, repo: IStorageRepository):
        self.repo = repo

    def _validate_item(self, item_dto) -> bool:
        pass

    def create(self, item_dto) -> bool:
        pass

    def get_all(self) -> list[ItemDto]:
        pass

    def find_by_name(self, name: str) -> ItemDto | None:
        pass

    def exists(self, name: str) -> bool:
        pass

    def update(self, item_dto) -> bool:
        pass

    def delete(self, name: str) -> bool:
        pass