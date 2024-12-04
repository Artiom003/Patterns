from abc import ABC, abstractmethod


class IScale(ABC):
    @abstractmethod
    def get_weight(self) -> float:
        pass


class RussianScales(IScale):
    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight


class BritishScales:
    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight


class AdapterForBritishScales(IScale):
    def __init__(self, british_scales: BritishScales):
        self.__british_scales = british_scales

    def get_weight(self) -> float:
        return self.__british_scales.get_weight() * .453


if __name__ == '__main__':
    kg: float = 55.  # кг
    lb: float = 55.  # фунты

    rScales = RussianScales(kg)
    bScales = AdapterForBritishScales(BritishScales(lb))

    print(rScales.get_weight())  # кг
    print(bScales.get_weight())  # кг


'''
Output:

55.0
24.915
'''


# «Прототип» - предназначен для использования функции объекта не доступного для модификации,
# используя специально созданный интерфейс.
# Т.е. позволяет объектам с несовместимыми интерфейсами работать вместе.