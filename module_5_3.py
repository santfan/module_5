# Создадим класс House с атрибутами name, number_of_floors
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

# Создадим два объекта класса House согластно условию
h_1 = House('ЖК Эльбрус', 10)
h_2 = House('ЖК Акация', 20)
# Убедимся что объекты создались
print(h_1)
print(h_2)
# Проверим работу магического метода __eq__
print(h_1 == h_2)
h_1 = h_1 + 10
# Посмотрим как отработал магический метод преобразования __add__
print(h_1)
# Теперь количество этажей объектов h_1 и h_2 равны проверим как отработает eq
print(h_1 == h_2)
print(h_1.__iadd__(10))
h2 = 10 + h_2
# Посмотрим как отработал магический метод отраженного присваивания __radd__
print(h_2)
# Магические методы сравнения
print(h_1 < h_2)
print(h_1 <= h_2)
print(h_1 > h_2)
print(h_1 >= h_2)
print(h_1 != h_2)