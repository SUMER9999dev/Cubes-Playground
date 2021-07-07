# import's
from Interfaces.IEvent import IEvent
from Interfaces.ICube import ICube
from Interfaces.IFactory import IFactory
from Interfaces.ICubeHandler import ICubeHandler

from Cubes.DefaultCube import DefaultCube


# factory
class DefaultFactory(IFactory):
    def __init__(self, handler_base: ICubeHandler) -> None:
        self.__handler_base: ICubeHandler = handler_base

    def create_cube(self, event: IEvent) -> ICube:
        cube = DefaultCube(100)
        cube.handler = self.__handler_base(event, cube)

        return cube
