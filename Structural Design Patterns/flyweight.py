from typing import List, Dict


class Shared:
    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class Unique:
    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__passport = passport

    @property
    def name(self):
        return self.__name

    @property
    def passport(self):
        return self.__passport


class Flyweight:
    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print('Отображаем новые данные: общие - {}_{}'.format(self.__shared.company, self.__shared.position),
              'и уникальные {}_{}'.format(unique.name, unique.passport))

    def get_data(self) -> str:
        return self.__shared.company + '_' + self.__shared.position


class FlyweightFactory:
    def get_key(self, shared: Shared):
        return '{}_{}'.format(shared.company, shared.position)

    def __init__(self, shareds: List[Shared]):
        self.__flyweights: Dict[str, Flyweight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)] = Flyweight(shared)

    def get_flyweight(self, shared: Shared):
        key: str = self.get_key(shared)
        if self.__flyweights.get(key) is None:
            print('Фабрика легковесов: Общий объект по ключу ' + key + ' не найден. Создаём новый.')
            self.__flyweights[key] = Flyweight(shared)
        else:
            print('Фабрика легковесов: Извлекаем данныые из имеющихся записей по ключу ' + key + '.')
        return self.__flyweights[key]

    def list_flyweights(self):
        count: int = len(self.__flyweights)
        print('\nФабрика легковесов: Всего {} записей:'.format(count))
        for pair in self.__flyweights.values():
            print(pair.get_data())


def add_specialist_database(ff: FlyweightFactory, company: str,
                            position: str, name: str, passport: str):
    print()
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, passport))


if __name__ == '__main__':
    shared_list: List[Shared] = (Shared('Microsoft', 'Управляющий'),
                                 Shared('Google', 'Android-разработчик'),
                                 Shared('Google', 'Web-разработчик'),
                                 Shared('Apple', 'IPhone-разработчик'))

    factory = FlyweightFactory(shared_list)
    factory.list_flyweights()

    add_specialist_database(factory,
                            'Google',
                            'Web-разработчик',
                            'Борис',
                            'AM-17234332')

    add_specialist_database(factory,
                            'Apple',
                            'Управляющий',
                            'Александр',
                            'DE-2211032')

    factory.list_flyweights()


'''
Output:

Фабрика легковесов: Всего 4 записей:
Microsoft_Управляющий
Google_Android-разработчик
Google_Web-разработчик
Apple_IPhone-разработчик

Фабрика легковесов: Извлекаем данныые из имеющихся записей по ключу Google_Web-разработчик.
Отображаем новые данные: общие - Google_Web-разработчик и уникальные Борис_AM-17234332

Фабрика легковесов: Общий объект по ключу Apple_Управляющий не найден. Создаём новый.
Отображаем новые данные: общие - Apple_Управляющий и уникальные Александр_DE-2211032

Фабрика легковесов: Всего 5 записей:
Microsoft_Управляющий
Google_Android-разработчик
Google_Web-разработчик
Apple_IPhone-разработчик
Apple_Управляющий
'''


# «Легковес»(приспособленец) - позволяет вместить большое количество объектов в отведённую оперативную память.
# Экономит память, выделяя и сохраняя общие параметры объектов.
# Однако при использовании паттерна, рассходуется процессорное время на поиск.
# Из-за введения доп классов усложняется код программы.
