# import's
from random import randint
import logging

from Interfaces.ICube import ICube
from Interfaces.ICubeHandler import ICubeHandler
from Interfaces.IEvent import IEvent


# logging
logger = logging.getLogger("DefaultCube")


# handler
class DefaultCubeHandler(ICubeHandler):
    def __init__(self, event_base: IEvent, owner: ICube) -> None:
        super().__init__(event_base, owner)

    def on_attack(self, enemy: ICube) -> None:
        damage = randint(1, 10)

        logger.debug(f"Beating {enemy} with damage: {damage}")

        enemy.handler.on_damage(damage)

    def on_damage(self, damage: int) -> None:
        if (self._owner.health - (damage - 1)) <= 0:
            self.on_die.notify(self._owner)
            return

        self._owner.health -= (damage - 1)

    @property
    def on_die(self) -> IEvent:
        return self._event


# cube
class DefaultCube(ICube):
    def __init__(self, health: int) -> None:
        super().__init__(health)

    @property
    def health(self) -> int:
        return self._hp

    @health.setter
    def health(self, new_health: int) -> None:
        self._hp = new_health

    def __repr__(self) -> str:
        return f"<DefaultCube hp={self.health}>"
