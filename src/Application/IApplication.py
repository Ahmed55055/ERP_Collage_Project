from abc import ABC, abstractmethod

class IApplication(ABC):

    @abstractmethod
    def build():
        pass

    @abstractmethod
    def run():
        pass