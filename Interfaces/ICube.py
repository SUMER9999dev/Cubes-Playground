# import's
from abc import ABC, abstractmethod


# interface
class ICube(ABC):
    def __init__(
        self, health: int
    ) -> None:
        """
        Just constructor

        :param health -> int:
        :return -> None:
        """
        self._hp = health
        self.handler = None  # handler -> ICubeHandler

    @property
    @abstractmethod
    def health(self) -> int:
        """
        return health

        :return -> int:
        """

    @health.setter
    def health(self, new_health: int) -> None:
        """
        Manager will call healt setter when you got damage.

        :param new_health -> int: new health value
        """
