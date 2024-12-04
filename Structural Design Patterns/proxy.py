from abc import ABC, abstractmethod
from typing import Dict


class ISite(ABC):
    @abstractmethod
    def get_page(self, num: int) -> str:
        pass


class Site(ISite):
    def get_page(self, num: int) -> str:
        return 'Это страница {}'.format(num)


class SiteProxy(ISite):
    def __init__(self, site: ISite):
        self.__site = site
        self.__cache: Dict[int, str] = {}

    def get_page(self, num: int) -> str:
        if self.__cache.get(num) is not None:
            page = self.__cache[num]
            page = 'из кэша: ' + page
        else:
            page = self.__site.get_page(num)
            self.__cache[num] = page
        return page


if __name__ == '__main__':
    my_site: ISite = SiteProxy(Site())

    print(my_site.get_page(1))
    print(my_site.get_page(2))
    print(my_site.get_page(3))

    print(my_site.get_page(2))


'''
Output:

Это страница 1
Это страница 2
Это страница 3
из кэша: Это страница 2
'''


# «Заместитель» - контролирует доступ к другому объекту, перехватывая все вызовы к нему,
# в клиент-серверном приложении применяется кеширование ранее полученных данных,
# тем самым снижается количество запросов к серверу.
