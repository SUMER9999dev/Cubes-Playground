# import's
from random import randint
import logging

from Interfaces.ICube import ICube
from Interfaces.IEvent import IEvent
from Interfaces.ICubeHandler import ICubeHandler


# setup logger
logger = logging.getLogger("MagicCube")


# handler
class MagicCubeHandler(ICubeHandler):
    def __init__(self, event_base: IEvent, owner: ICube) -> None:
        super().__init__(event_base, owner)

    def on_attack(self, enemy: ICube) -> None:
        fireball_damage = randint(10, 25)
        logger.debug(
            f'Created fireball with damage {fireball_damage} for {enemy}.'
        )

        enemy.handler.on_damage(fireball_damage)

    def on_damage(self, damage: int) -> None:
        heal = randint(1, 5)

        if (self._owner.health - (damage - heal)) <= 0:
            self.on_die.notify(self._owner)
            return

        logger.debug(f'healing for {heal} hp.')

        self._owner.health -= damage - heal

    @property
    def on_die(self) -> IEvent:
        return self._event


# cube
class MagicCube(ICube):
    def __init__(
        self, health: int, magic_power: int
    ) -> None:
        super().__init__(health)
        self.__magic_power = magic_power

    @property
    def health(self) -> int:
        return self._hp

    @health.setter
    def health(self, new_health: int):
        self._hp = new_health

    def __repr__(self) -> str:
        return f"<MagicCube hp={self.health} power={self.__magic_power}>"
