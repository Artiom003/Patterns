from abc import ABC, abstractmethod


class IProcessor(ABC):

    @abstractmethod
    def process(self):
        pass


class Transmitter(IProcessor):
    def __init__(self, data: str):
        self.__data = data

    def process(self):
        print('Данные {} переданы по каналу связи'.format(self.__data))


class Shell(IProcessor):
    def __init__(self, pr: IProcessor):
        self._processor = pr

    @abstractmethod
    def process(self):
        self._processor.process()


class HammingCoder(Shell):
    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print('Наложен помехоустойчивый код Хэмминг->', end='')
        self._processor.process()


class Encryptor(Shell):
    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print('Шифрование->', end='')
        self._processor.process()


if __name__ == '__main__':
    transmitter: IProcessor = Transmitter('12345')
    transmitter.process()
    print()

    hamming_coder: Shell = HammingCoder(transmitter)
    hamming_coder.process()
    print()

    encryptor: Shell = Encryptor(hamming_coder)
    encryptor.process()

'''
Output:

Данные 12345 переданы по каналу связи

Наложен помехоустойчивый код Хэмминг->Данные 12345 переданы по каналу связи

Шифрование->Наложен помехоустойчивый код Хэмминг->Данные 12345 переданы по каналу связи
'''


# «Декоратор» - предназначен для динамического подключения дополнительного поведения объекту.
# Предоставляет создание подклассов с целью расширения функциональности.
