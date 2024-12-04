from abc import ABC, abstractmethod
from typing import List


class IObserver(ABC):
    @abstractmethod
    def update(self, p: int):
        pass


class IObservable(ABC):
    @abstractmethod
    def add_observer(self, o: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, o: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(IObservable):
    def __init__(self, price: int):
        self.__price = price
        self.__observers: List[IObserver] = []

    def change_price(self, price: int):
        self.__price = price
        self.notify()

    def add_observer(self, o: IObserver):
        self.__observers.append(o)

    def remove_observer(self, o: IObserver):
        self.__observers.remove(o)

    def notify(self):
        for o in self.__observers:
            o.update(self.__price)


class Wholesale(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 300:
            print('Оптовик закупил товар по цене {}'.format(p))
            self.__product.remove_observer(self)


class Buyer(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 350:
            print('Покупатель закупил товар по цене {}'.format(p))
            self.__product.remove_observer(self)


if __name__ == '__main__':

    product = Product(400)

    wholesale = Wholesale(product)
    buyer = Buyer(product)

    product.change_price(320)
    product.change_price(280)


'''
Output:

Покупатель закупил товар по цене 320
Оптовик закупил товар по цене 280
'''


# «Наблюдатель» - позволяет одним объектам следить и реагировать на события,
# происходящие в других объектах.
