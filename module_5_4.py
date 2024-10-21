class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # Дополним класс магическим методом __eq__. Метод принимает два атрибута
    # Магический метод __eq__ еще можно называть методом эквивалентности
    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    # Магические методы сравнения
    # Магический метод __lt__ метод меньше (<)
    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    # Магический метод __le__ метод меньше или равно (<=)
    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    # Магический метод __gt__ метод больше (>)
    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    # Магический метод __ge__ метод больше или равно (>=)
    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    # Магический метод __ne__ метод не равно (!=)
    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    # Дополним класс еще одним магическим методом __add__
    def __add__(self, num):
        if isinstance(num, int):
            self.number_of_floors = self.number_of_floors + num
        return self

    # Собственно методы __iadd__ и __radd__ Это разные формы метода __add__
    # Магический метод __radd__ еще называется отраженным присваиванием
    def __radd__(self, num):
        return self.__add__(num)

    # Магический метод __iadd__ еще называется сложением с присваиванием
    def __iadd__(self, num):
        if isinstance(num, int):
            self.number_of_floors += num
        return self

    # Создадим пустой список принадлежащий классу House
    house_history = []

    # Создадим правила заполнения списка в методе __new__
    def __new__(cls, *args):
        cls.house_history.append(args[0])
        # Вернем дополненый список в пространство имен класса
        return object.__new__(cls)

    # Инициируем создание объекта
    def __init_(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Пропишем магический метод __del__
    def __del__(self):
        # Выведем результат магического метода
        print(f'{self.name} снесен но память о нем останется в истории')


# Создадим объекты класса House и выведем изменение переменной класса house_history
h_1 = House('ЖК Эльбрус', 10)
print(House.house_history)
h_2 = House('ЖК Жемчужина', 20)
print(House.house_history)
h_3 = House('ЖК Самоделкин', 5)
print(House.house_history)

# Удаление созданных объектов
del h_2
del h_3

# Проверим что содержимое объекта класса не изменилось не смотря на удаления
print(House.house_history)
