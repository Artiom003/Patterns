from abc import ABC


class Phone:
    def __init__(self):
        self.data: str = ''

    def about_phone(self) -> str:
        return self.data

    def append_data(self, string: str):
        self.data += string


class IDeveloper(ABC):
    def create_display(self):
        pass

    def create_box(self):
        pass

    def system_install(self):
        pass

    def get_phone(self) -> Phone:
        pass


class AndroidDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Произведён дисплей Samsung; ')

    def create_box(self):
        self.__phone.append_data('Произведён корпус Samsung; ')

    def system_install(self):
        self.__phone.append_data('Установлена система Android; ')

    def get_phone(self) -> Phone:
        return self.__phone


class IphoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Произведён дисплей Iphone; ')

    def create_box(self):
        self.__phone.append_data('Произведён корпус Iphone; ')

    def system_install(self):
        self.__phone.append_data('Установлена система IOS; ')

    def get_phone(self) -> Phone:
        return self.__phone


class Director:
    def __init__(self, developer: IDeveloper):
        self.__developer = developer

    def set_developer(self, developer: IDeveloper):
        self.__developer = developer

    def mount_only_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        return self.__developer.get_phone()

    def mount_full_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        self.__developer.system_install()
        return self.__developer.get_phone()


if __name__ == '__main__':

    android_developer: IDeveloper = AndroidDeveloper()

    director = Director(android_developer)

    samsung: Phone = director.mount_full_phone()
    print(samsung.about_phone())

    iphone_developer: IDeveloper = IphoneDeveloper()

    director.set_developer(iphone_developer)

    iphone: Phone = director.mount_only_phone()
    print(iphone.about_phone())


'''
Output:

Произведён корпус Samsung; Произведён дисплей Samsung; Установлена система Android; 
Произведён корпус Iphone; Произведён дисплей Iphone; 
'''


# «Строитель», который предоставляет способ создания составного объекта.
# Он отделяет конструирование сложного объекта от его представления так,
# что в результате одного и того же процесса конструирования могут получаться разные представления.
# Паттерн позволяет изменять внутреннее представление продукта,
# изолирует код, реализующий представление продукта.
