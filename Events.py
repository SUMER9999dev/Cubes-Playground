# import's
from typing import Callable

from Interfaces.IEvent import IEvent


# events
class Event(IEvent):
    def __init__(self) -> None:
        super().__init__()

    def notify(self, *args, **kwargs) -> None:
        for observer in self._observers:
            observer(*args, **kwargs)

    def deattach(self, observer: Callable[[any], None]) -> None:
        self._observers.remove(observer)

    def attach(self, observer: Callable[[any], None]) -> None:
        self._observers.append(observer)
