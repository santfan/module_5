# Создадим класс объектов House
class House():
  # Инициируем созданный класс с атрибутами name и numbers_of_floos
  def __init__(self, name, numbers_of_floos):
    self.name = name
    self.numbers_of_floos = numbers_of_floos

# Создадим два объекта класса House согластно условию
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Убедимся что объекты создались
print(h1.name, h1.numbers_of_floos)
print(h2.name, h2.numbers_of_floos)

# Продублируем создание класса объектов House
class House():
  # Инициируем созданный класс с атрибутами name и numbers_of_floos
  def __init__(self, name, numbers_of_floos):
    self.name = name
    self.numbers_of_floos = numbers_of_floos
  # Добавим магический метод __str__
  def __str__(self):
    return f'Название: {self.name}, количество этажей: {self.numbers_of_floos}'
  # Добавим магический метод __len__
  def __len__(self):
    return self.numbers_of_floos

# Создадим два объекта класса House согластно условию
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Проверим как работает магический метод __len__
print(len(h1))
print(len(h2))

# Проверим как работает магический метод __str__
print(h1)
print(h2)

'''Итог:
1. Создан класс объектов House с атрибутами name и numbers_of_floos
2. Созданы два объекта h1 и h2 класса House с разными для каждого объкта
значениями атрибутов
3. Внутри класса House созданы два магических метода __str__ и __len__'''