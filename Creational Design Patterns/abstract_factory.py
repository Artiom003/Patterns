from abc import ABC, abstractmethod


class IEngine(ABC):
    @abstractmethod
    def release_engine(self):
        pass


class JapaneseEngine(IEngine):
    def release_engine(self):
        print('японский двигатель')


class RussianEngine(IEngine):
    def release_engine(self):
        print('российский двигатель')


class ICar(ABC):
    @abstractmethod
    def release_car(self, engine: IEngine):
        pass


class JapaneseCar(ICar):
    def release_car(self, engine: IEngine):
        print('Собрали японский автомобиль, ', end='')
        engine.release_engine()


class RussianCar(ICar):
    def release_car(self, engine: IEngine):
        print('Собрали российский автомобиль, ', end='')
        engine.release_engine()


class IFactory(ABC):
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass


class JapaneseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return JapaneseEngine()

    def create_car(self) -> ICar:
        return JapaneseCar()


class RussianFactory(IFactory):
    def create_engine(self) -> IEngine:
        return RussianEngine()

    def create_car(self) -> ICar:
        return RussianCar()


if __name__ == '__main__':

    j_factory = JapaneseFactory()
    j_engine = j_factory.create_engine()
    j_car = j_factory.create_car()

    j_car.release_car(j_engine)

    r_factory = RussianFactory()
    r_engine = r_factory.create_engine()
    r_car = r_factory.create_car()

    r_car.release_car(r_engine)


'''
Output:

Собрали японский автомобиль, японский двигатель
Собрали российский автомобиль, российский двигатель
'''


#  «Абстрактная фабрика» - предоставляет интерфейс для создания
#  взаимосвязанных или взаимозависимых объектов.
#  Используется, когда программа должна быть независимой от процессов и типов,
#  создаваемых новых объектов. Упрощает замену семейств продуктов.
#  Недостатком является сложность добавления нового продукта в фабрику.
