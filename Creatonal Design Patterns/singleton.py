class DataBaseHelper:
    __database_connection = None
    __data: str = ''

    def __new__(cls):
        if cls.__database_connection is None:
            cls.__database_connection: DataBaseHelper = object.__new__(cls)
            print('Подключение к БД')
        return cls.__database_connection

    def select_data(self) -> str:
        return self.__data

    def insert_data(self, new_data: str):
        self.__data = new_data


if __name__ == '__main__':
    connection1 = DataBaseHelper()
    connection1.insert_data('123')

    connection2 = DataBaseHelper()
    print(connection2.select_data())


'''
Output:

Подключение к БД
123
'''


# «Одиночка», который гарантирует, что в приложении будет создан единственный
# экземпляр некоторого класса и предоставляет глобальную точку доступа к этому экземпляру.

