# import's
from Factories.DefaultFactory import DefaultFactory
from Factories.MagicFactory import MagicFactory

from Cubes.MagicCube import MagicCubeHandler
from Cubes.DefaultCube import DefaultCubeHandler

from Storages.MemoryStorage import MemoryStorage

from Manager import Manager


# run
def main():
    factories = [DefaultFactory(DefaultCubeHandler), MagicFactory(MagicCubeHandler)]

    storage = MemoryStorage()

    manager = Manager(factories, storage)

    how_many_cubes = int(input("How many cubes you want: "))
    how_many_iterations = int(input("How many iterations you want: "))

    for _ in range(how_many_cubes):
        manager.new_cube()

    for _ in range(how_many_iterations):
        manager.fight()

    print("All alive cubes:", storage.get_all_cubes())
    input("Press enter to exit...")


if __name__ == "__main__":
    main()
