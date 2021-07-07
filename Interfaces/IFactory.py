# import's
from abc import ABC, abstractmethod

from Interfaces.ICube import ICube
from Interfaces.ICubeHandler import ICubeHandler
from Interfaces.IEvent import IEvent


# interface
class IFactory(ABC):
    @abstractmethod
    def __init__(self, handler_base: ICubeHandler) -> None:
        pass

    @abstractmethod
    def create_cube(self, event: IEvent) -> ICube:
        """
        creating new cube

        :return -> ICube:
        """
