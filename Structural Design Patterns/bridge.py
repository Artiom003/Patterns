from abc import ABC, abstractmethod


class IDataReader(ABC):
    @abstractmethod
    def read(self):
        pass


class DatabaseReader(IDataReader):
    def read(self):
        print('Данные из базы данных ', end='')


class FileReader(IDataReader):
    def read(self):
        print('Данные из файла ', end='')


class Sender(ABC):
    def __init__(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader

    def set_data_reader(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader

    @abstractmethod
    def send(self):
        pass


class EmailSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('отправлены при помощи Email')


class TelegramBotSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('отправлены при помощи Telegram бота')


if __name__ == '__main__':
    sender: Sender = EmailSender(DatabaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()

    sender = TelegramBotSender(DatabaseReader())
    sender.send()


'''
Output:

Данные из базы данных отправлены при помощи Email
Данные из файла отправлены при помощи Email
Данные из базы данных отправлены при помощи Telegram бота
'''


# «Мост» - разделяет абстракцию и реализацию так, чтобы они могли изменяться независимо.
# Использует инкапсуляцию, агрегирование и может использовать наследование,
# чтобы разделить ответственность между классами.

