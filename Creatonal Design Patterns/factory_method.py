from abc import ABC, abstractmethod


class IProduct(ABC):
    @abstractmethod
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print('Выпущен новый легковой автомобиль')


class Truck(IProduct):
    def release(self):
        print('Выпущен грузовой автомобиль')


class IWorkShop(ABC):
    @abstractmethod
    def create(self) -> IProduct:
        pass


class CarWorkShop(IWorkShop):
    def create(self):
        return Car()


class TruckWorkShop(IWorkShop):
    def create(self):
        return Truck()


if __name__ == '__main__':
    creator = CarWorkShop()
    car = creator.create()

    creator = TruckWorkShop()
    truck = creator.create()

    car.release()
    truck.release()

'''
Output:

Выпущен новый легковой автомобиль
Выпущен грузовой автомобиль
'''

#  «Фабричный метод» - предоставляет интерфейс для создания экземпляров некоторого класса.
#  В момент создания наследники могут определить какой класс создавать.
#  Недостатком паттерна является необходимость создавать наследника для каждого нового типа.
