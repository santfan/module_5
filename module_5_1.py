# Создадим класс объектов House
class House():
  # Инициируем созданный класс с атрибутами name и numbers_of_floos
  def __init__(self, name, numbers_of_floos):
    self.name = name
    self.numbers_of_floos = numbers_of_floos

# Создадим два объекта класса House согластно условию
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Убедимся что объекты создались
print(h1.name, h1.numbers_of_floos)
print(h2.name, h2.numbers_of_floos)

# Продублируем создание класса объектов House
class House():
  # Инициируем созданный класс с атрибутами name и numbers_of_floos
  def __init__(self, name, numbers_of_floos):
    self.name = name
    self.numbers_of_floos = numbers_of_floos
  # Добавим метод go_to с атрибутом new_floos
  def go_to(self, new_floos):
    # Добавим логику согластно условию
    if self.numbers_of_floos < new_floos or new_floos < 1:
      print('Такого этажа не существует')
    else:
      for i in range(1, new_floos + 1):
        print(i)

# Создадим два объекта класса House согластно условию
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# Проверим как работает созданый для объектов метод
h1.go_to(5)
h2.go_to(10)

'''Итог:
1. Создан класс объектов House с атрибутами name и numbers_of_floos
2. Созданы два объекта h1 и h2 класса House с разными для каждого объкта
значениями атрибутов
3. Внутри класса House создан метод go_to c атрибутом new_floos
4. Внутри метода go_to реализована логика согластно условию задачи'''
