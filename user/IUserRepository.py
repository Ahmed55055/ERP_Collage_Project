from abc import ABC, abstractmethod
from typing import List
from .dto import UserDto


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user_dto) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> List[UserDto]:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> UserDto | None:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> UserDto | None:
        pass

    @abstractmethod
    def exists(self, username: str) -> bool:
        pass

    @abstractmethod
    def update(self, user_dto) -> bool:
        pass

    @abstractmethod
    def delete(self, username: str) -> bool:
        pass