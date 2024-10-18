from random import randint
import requests
from datetime import datetime, timedelta



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
        self.last_feed_time = datetime.now
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
        if self.feed >= 1:    
            self.feed -=  1
            self.level += 0.5
            self.hp += randint(5,10)
            return f'Вы успешно покормили своего покемона! Количество еды для покемона: {self.feed}, его уровень: {self.level}, его здоровье:{self.hp}'
        else:
            return'У вас нет доступной еды для покемона!'
        
    def feed3(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  
            

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
            chance2 = randint(1,10)
            #self.hp = randint(70,110)
            #self.power = randint(5,15)
            if chance2 >= 7:
                return f"Покемон-волшебник({enemy.pokemon_trainer}) применил щит в сражении"
        if enemy.hp > self.power:
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
    def feed3(self):
        super().feed3(feed_interval=10)

class Fighter(Pokemon):
    def attack(self, enemy):
        #self.hp = randint(40, 70)
        #self.power = randint(15,30)
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    def feed3(self):
        super().feed3(hp_increase=20)


