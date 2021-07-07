# import's
from random import randint

from Interfaces.ICube import ICube
from Interfaces.IFactory import IFactory
from Interfaces.ICubeHandler import ICubeHandler
from Interfaces.IEvent import IEvent

from Cubes.MagicCube import MagicCube


# factory
class MagicFactory(IFactory):
    def __init__(self, handler_base: ICubeHandler) -> None:
        self.__handler_base: ICubeHandler = handler_base

    def create_cube(self, event: IEvent) -> ICube:
        magic_power = randint(1, 3)
        cube = MagicCube(75, magic_power)

        cube.handler = self.__handler_base(event, cube)

        return cube
