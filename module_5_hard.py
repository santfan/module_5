# Для имитации видеоконьента импортитруем модуль
import time
'''Объявим класс пользователей платформы Урбан Университет. При инициации
  пользователей принимаются аргуметы Имя пользователя, хешированный пароль,
  возраст зарегистрированного пользователя'''
class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname
'''Объявим класс содержащий видеоконтент . При инициации
  видео принимаются аргуметы название видео, продолжительность видео,
  возрастной ограничитель установлен в положение False'''
class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
# Две функции отвечающие за поиск по коллекции видео
    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title
'''Объявим класс собственной самой видеоплатформы.'''
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
# Функция регистрации пользователя. Пароль принимается в виде строки
    def register(self, nickname: str, password: str, age: int):
        # Пароль жоджен содержать хотя бы одну заглавную букву
        if not any(__.isupper() for __ in password):
          print('Пароль должен содержать хотя бы одну заглавную букву')
          return
        # Пароль должен содержать хотя бы одну цифру
        if not any(__.isdigit() for __ in password):
          print('Пароль не отвечает требованием безопасности')
          return
        # Пароль дожен быть не менее 8 символов
        if len(password) < 8:
          print('Пароль не отвечает требованием безопасности')
          return
        # Передаим пароль в хешированном виде
        password = hash(password)
        for user in self.users:
          # Проверим есть ли пользователь в базе
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        # Добавим нового пользователя
        self.users.append(new_user)
        # Установим текущего пользователя
        self.current_user = new_user
# Функция выхода пользователя
    def log_out(self):
        self.current_user = None
# Функция входа уже зарегистрированного пользователя
    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user
# Функция добавления видео в контент
    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)
# Функция загрузки видео
    def get_videos(self, text: str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie
# Проверка права пользователя на просмотр
    def watch_video(self, movie: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return
# Собственно имитация видео
                for i in range(1, 11):
                    print(i, end=' ')
                    time.sleep(1)
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')

if __name__ == '__main__':
# Обработка в точке входа
    ur = UrTube()
    v_1 = Video('Лучший язык программирования 2024 года', 200)
    v_2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v_1, v_2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheurek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Такого видео нет')

