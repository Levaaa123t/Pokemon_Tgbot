from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, level = 0, feed = 0):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.feed = feed
        self.level = level
        Pokemon.pokemons[pokemon_trainer] = self
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return 'https://static.wikia.nocookie.net/anime-characters-fight/images/7/77/Pikachu.png/revision/latest/scale-to-width-down/700?cb=20181021155144&path-prefix=ru'
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    def give_food(self):
        self.feed +=  1
        self.level += 0.5
        return f'Вы успешно покормили своего покемона! Количетсво раз сколько его кормили: {self.feed}, его уровень: {self.level}'
        #elif self.feed <= 1:
         #   self.feed += 1
          #  self.level += 0.5

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}, его уровень: {self.level}, количество раз сколько его кормили: {self.feed}"
        
    def about_level(self):
        return f'Уровень твоего покемона: {self.level}'
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img




