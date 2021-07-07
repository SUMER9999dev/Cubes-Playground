# import's
from abc import ABC, abstractmethod

import Interfaces.ICube as ICube
from Interfaces.IEvent import IEvent


# ICubeHandler
class ICubeHandler(ABC):
    def __init__(self, event_base: IEvent, owner: ICube.ICube) -> None:
        self._owner = owner
        self._event = event_base

    @abstractmethod
    def on_damage(self, damage: int) -> None:
        '''
        handle damage

        :param damage -> int:
        :return -> None:
        '''

    @abstractmethod
    def on_attack(self, enemy: ICube.ICube) -> None:
        '''
        attacks enemy

        :param enemy -> ICube:
        :return -> None:
        '''

    @property
    @abstractmethod
    def on_die(self) -> IEvent:
        '''
        will return on_die event

        :return -> IEvent:
        '''
