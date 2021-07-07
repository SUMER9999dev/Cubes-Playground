# import's
from abc import ABC, abstractmethod
from typing import Callable


# IEvent
class IEvent(ABC):
    def __init__(self) -> None:
        self._observers = []

    @abstractmethod
    def attach(self, observer: Callable[[any], None]) -> None:
        """
        attach new observer to event

        :param observer -> Callable[[any], None]:
        """

    @abstractmethod
    def deattach(self, observer: Callable[[any], None]) -> None:
        """
        deattach observer from event

        :param observer -> Callable[[any], None]:
        """

    @abstractmethod
    def notify(self, *args, **kwargs) -> None:
        """
        will notify all observers
        """
