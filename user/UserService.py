from .IUserService import IUserService
from .IUserRepository import IUserRepository
from .dto import UserDto
from typing import List


class UserService(IUserService):
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def create(self, user_dto) -> bool:
        pass

    def get_all(self) -> List[UserDto]:
        pass

    def find_by_username(self, username: str) -> UserDto | None:
        pass

    def find_by_email(self, email: str) -> UserDto | None:
        pass

    def exists(self, username: str) -> bool:
        pass

    def update(self, user_dto) -> bool:
        pass

    def delete(self, username: str) -> bool:
        pass