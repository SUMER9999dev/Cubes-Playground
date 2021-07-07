# import's
from typing import Optional

from Interfaces.IStorage import IStorage
from Interfaces.ICube import ICube


# storage
class MemoryStorage(IStorage):
    def __init__(self, base_cubes: Optional[list[ICube]] = None) -> None:
        self.__cubes = base_cubes if base_cubes is not None else []

    def remove_cube(self, cube: ICube) -> None:
        return self.__cubes.remove(cube)

    def get_all_cubes(self) -> list[ICube]:
        return self.__cubes

    def add_cube(self, cube: ICube) -> bool:
        self.__cubes.append(cube)
        return True
