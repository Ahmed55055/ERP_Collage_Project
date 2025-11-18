from abc import ABC, abstractmethod

from ..dto import ItemDto


class IStorageService(ABC):

    @abstractmethod
    def create(self, item_dto) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> list[ItemDto]:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> ItemDto | None:
        pass

    @abstractmethod
    def exists(self, name: str) -> bool:
        pass

    @abstractmethod
    def update(self, item_dto) -> bool:
        pass

    @abstractmethod
    def delete(self, name: str) -> bool:
        pass