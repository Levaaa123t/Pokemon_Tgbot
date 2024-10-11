from random import randint
import requests


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, level = 0, feed = 1):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.feed = feed
        self.level = level
        self.hp = randint(50, 100)
        self.power = randint(10,20)
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
        if self.feed <= 1:    
            self.feed -=  1
            self.level += 0.5
            self.hp += randint(5,10)
            return f'Вы успешно покормили своего покемона! Количество еды для покемона: {self.feed}, его уровень: {self.level}, его здоровье:{self.hp}'
        #elif self.feed <= 1:
         #   self.feed += 1
          #  self.level += 0.5
        else:
            return'У вас нет доступной еды для покемона!'

    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покемона: {self.name}
    Уровень твоего покемона: {self.level}
    Количество еды для покемона: {self.feed}
    Количество жизней:{self.hp}
    Сила покемона: {self.power}
"""
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance2 = randint(1,5)
            if chance2 == 1 or 2:
                return "Покемон-волшебник применил щит в сражении"
        elif enemy.hp > self.power:
            enemy.hp -= self.power
            return f"""Сражение {self.pokemon_trainer} с {enemy.pokemon_trainer}
Здоровье покемона @{self.pokemon_trainer}:{self.hp}
Здоровье покеомна @{enemy.pokemon_trainer}: {enemy.hp}
"""
        else:
            enemy.hp = 0
            return f"Победа {self.pokemon_trainer} над {enemy.pokemon_trainer}! "
    def about_level(self):
        self.level += 1
        return f'Уровень твоего покемона: {self.level}, количество еды для покемона:{self.feed}'
        
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "


