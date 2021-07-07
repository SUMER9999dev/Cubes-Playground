# import's
from random import choice, shuffle
import logging

from Interfaces.IFactory import IFactory
from Interfaces.IStorage import IStorage
from Interfaces.ICube import ICube

from Events import Event


# setup logger
logger = logging.getLogger("Manager")


# manager
class Manager():
    def __init__(self, cube_factories: list[IFactory], cube_storage: IStorage):
        self.__factories = cube_factories
        self._storage = cube_storage

    def __on_cube_die(self, cube: ICube):
        cube.handler.on_die.deattach(self.__on_cube_die)

        self._storage.remove_cube(cube)
        logger.debug(f"Cube {cube} die.")

    def new_cube(self, cube: ICube = None) -> bool:
        if cube is None:
            factory = choice(self.__factories)

            cube = factory.create_cube(Event())
            cube.handler.on_die.attach(self.__on_cube_die)

            return self._storage.add_cube(cube)

        return self._storage.add_cube(cube)

    def fight(self) -> None:
        cubes = self._storage.get_all_cubes()
        shuffle(cubes)

        if len(cubes) == 1:
            raise Exception("Can't fight with my self.")

        for index, cube in enumerate(cubes):
            if (len(cubes) - 1) == index:
                logger.debug(f"cube {cube} lose his battle.")
                break

            logger.debug(f"update cube with id {index}")

            cube_enemy = choice(list(filter(lambda x: x != cube, cubes)))

            cube.handler.on_attack(cube_enemy)
