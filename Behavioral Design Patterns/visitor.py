from abc import ABC, abstractmethod
from typing import List


class IVisitor(ABC):
    @abstractmethod
    def visit(self, place: 'IPlace'):
        pass


class IPlace(ABC):
    @abstractmethod
    def accept(self, visitor: IVisitor):
        pass


class Zoo(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class Cinema(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class Circus(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class HolidayMarket(IVisitor):
    def __init__(self):
        self.value = ''

    def visit(self, place: IPlace):
        if isinstance(place, Zoo):
            self.value = 'Слон в зоопарке'
        elif isinstance(place, Cinema):
            self.value = 'Кино - Властелин колец'
        elif isinstance(place, Circus):
            self.value = 'Клоун в цирке'


if __name__ == '__main__':
    places: List[IPlace] = [Zoo(), Cinema(), Circus()]
    visitor = HolidayMarket()

    for place in places:
        place.accept(visitor)
        print(visitor.value)


'''
Output:

Слон в зоопарке
Кино - Властелин колец
Клоун в цирке
'''

# «Посетитель», позволяющий добавлять в программу новые операции,
# не изменяя классы объектов, над которыми эти операции могут выполняться.
# Преимуществом паттерна является то,
# что он объединяет родственный операции в одном классе,
# упрощает добавление операций, работающих со сложными структурами объектов.
# Отрицательным моментом является возможное нарушение инкапсуляции элементов.
