from random import randint
import requests
from datetime import datetime, timedelta



class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, level = 0, count_feed = 1):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.count_feed = count_feed
        self.level = level
        self.hp = randint(50, 100)
        self.power = randint(10,20)
        self.last_feed_time = datetime.now()
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
    #def give_food(self):
     #   if :    
      #      
        #    self.hp += randint(5,10)
         #   return f'Вы успешно покормили своего покемона! Количество еды для покемона: {self.feed}, его уровень: {self.level}, его здоровье:{self.hp}'
        #else:
         #   return'У вас нет доступной еды для покемона!'
        
    def feed3(self, feed_interval = 20, hp_increase = randint(10,15) ):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time and self.count_feed >= 1:
            self.count_feed -=  1
            self.level += 0.5
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}, текущий уровень: {self.level}, количество еды для покемона: {self.count_feed}"
        else:
            return f"""Вы не можете покормить вашего покемона если с последнего кормления не прошло 20 секунд и у вас нет еды.
        Следующее время кормления покемона: {current_time+delta_time}, количетсво еды для покемона: {self.count_feed}
        """ 
            

    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покемона: {self.name}
    Уровень твоего покемона: {self.level}
    Количество еды для покемона: {self.count_feed}
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
        if self.hp <= 0:
                return f'{self.pokemon_trainer} Не может атаковать так как имеет 0 здоровья!'
        if enemy.hp > self.power:
            enemy.hp -= self.power
            if enemy.hp <= 0:
                self.count_feed = 1
                self.level = 2
                return f"Победа {self.pokemon_trainer} над {enemy.pokemon_trainer}! Ваш уровень = {self.level}, ваше количество еды = {self.count_feed}"
            
            return f"""Сражение {self.pokemon_trainer} с {enemy.pokemon_trainer}
Здоровье покемона {self.pokemon_trainer}:{self.hp}
Здоровье покемона {enemy.pokemon_trainer}: {enemy.hp}
"""
    def about_level(self):
        return f'Уровень твоего покемона: {self.level}, количество еды для покемона:{self.count_feed}'
        
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Wizard(Pokemon):
    def feed_wizzard(self):
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
    def feed_fighter(self):
        super().feed3(hp_increase=20)



