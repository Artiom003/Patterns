from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def parse(self, url: str):
        pass


class ResourceReader:
    def __init__(self, reader: Reader):
        self.__reader = reader

    def set_strategy(self, reader: Reader):
        self.__reader = reader

    def read(self, url: str):
        self.__reader.parse(url)


class NewSiteReader(Reader):
    def parse(self, url: str):
        print('Парсинг новостного сайта:', url)


class SocialNetworkReader(Reader):
    def parse(self, url: str):
        print('Парсинг ленты новостей социальной сети:', url)


class TelegramChannelReader(Reader):
    def parse(self, url: str):
        print('Парсин Telegram-канала:', url)


if __name__ == '__main__':
    resource_reader = ResourceReader(NewSiteReader())

    url = 'https://news.com'
    resource_reader.read(url)

    resource_reader.set_strategy(SocialNetworkReader())

    url = 'https://facebook.com'
    resource_reader.read(url)

    resource_reader.set_strategy(TelegramChannelReader())

    url = '@news_channel_telegram'
    resource_reader.read(url)


'''
Output:

Парсинг новостного сайта: https://news.com
Парсинг ленты новостей социальной сети: https://facebook.com
Парсин Telegram-канала: @news_channel_telegram
'''

#  «Стратегия» - определяет семейство схожих алгоритмов и помещает каждый из них в собственный класс.
#  Положительными моментами является то, что паттерн изолирует код алгоритмов от остальных классов,
#  алгоритмы можно быстро заменять, во время выполнения программы.
