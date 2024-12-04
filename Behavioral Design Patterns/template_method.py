from abc import ABC, abstractmethod


class Transmitter(ABC):
    def _voice_record(self):
        print('Запись фрагмента речи')

    def _simpling(self):
        pass

    def _digitization(self):
        pass

    @abstractmethod
    def _modulation(self):
        pass

    def _transmission(self):
        print('Передача сигнала по радиоканалу')

    def process_start(self):
        self._voice_record()
        self._simpling()
        self._digitization()
        self._modulation()
        self._transmission()


class AnalogTransmitter(Transmitter):
    def _modulation(self):
        print('Модуляция аналогового сигнала')


class DigitTransmitter(Transmitter):
    def _simpling(self):
        print('Дискретизация записанного фрагмента')

    def _digitization(self):
        print('Оцифровка')

    def _modulation(self):
        print('Модуляция цифрового сигнала')


if __name__ == '__main__':
    analog_transmitter = AnalogTransmitter()
    analog_transmitter.process_start()

    print()

    digit_transmitter = DigitTransmitter()
    digit_transmitter.process_start()


'''
Output:

Запись фрагмента речи
Модуляция аналогового сигнала
Передача сигнала по радиоканалу

Запись фрагмента речи
Дискретизация записанного фрагмента
Оцифровка
Модуляция цифрового сигнала
Передача сигнала по радиоканалу
'''


# «Шаблонный метод» - определяет основу алгоритма
# и позволяет наследникам переопределять некоторые шаги алгоритма,
# не изменяя его структуру в целом. Преимуществом паттерна является то,
# что он облегчает повторное использование кода.
