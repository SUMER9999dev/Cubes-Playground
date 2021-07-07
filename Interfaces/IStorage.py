# import's
from abc import ABC, abstractmethod
from typing import Optional

from Interfaces.ICube import ICube


# interface
class IStorage(ABC):
    def __init__(self, base_cubes: Optional[list[ICube]] = None) -> None:
        """
        Just constructor

        :param base_cubes -> Optional[list[ICube]]: default cubes to storage
        """

    @abstractmethod
    def add_cube(self, cube: ICube) -> bool:
        """
        add new cube to cube storage

        :param cube -> ICube: cube to store
        :return -> bool: return True if complete
        """

    @abstractmethod
    def remove_cube(self, cube: ICube) -> None:
        """
        delete cube from storage

        :param cube -> ICube: cube to delete
        :return -> None:
        """

    @abstractmethod
    def get_all_cubes(self) -> list[ICube]:
        """
        return all cubes

        :return -> list[ICube]:
        """
