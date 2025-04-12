# coding=utf-8
from random import randint
import requests


class Pokemon:
    
    pokemons = {}
    
    
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.front_img = self.get_front_img()
        self.back_img = self.get_back_img()
        self.name = self.get_name()
        if randint(0, 500) == 0:
            self.is_super = True
        else:
            self.is_super = False
        self.normal_hp = randint(10, 50)
        self.normal_power = randint(1, 5)
        if self.is_super:
            self.normal_hp += 20
            self.normal_power += 2
        self.current_hp = self.normal_hp
        self.current_power = self.normal_power
        Pokemon.pokemons[pokemon_trainer] = self
    
    
    # Метод для получения картинки покемона через API
    def get_front_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    
    
    def get_back_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['back_default']
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png"
    
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            return "Pikachu"
    
    
    def attack(self, enemy):
        if enemy.current_hp > self.current_power:
            if isinstance(enemy, Wizard):
                if randint(1, 5) == 1:
                    return "Покемон-волшебник применил щит в сражении"
            enemy.current_hp -= self.current_power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.current_hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    
    
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}, его класс - {"Волшебник" if isinstance(self, Wizard) else "Боец"}, он {"Редкий" if self.is_super else "Обычный"}"
    
    
    # Метод класса для получения картинки покемона
    def show_front_img(self):
        return self.front_img
    
    
    def show_back_img(self):
        return self.back_img


class Wizard(Pokemon):
    def __init__(self, pokemon_trainer_):
        super().__init__(pokemon_trainer_)
        self.normal_hp += 10
        self.current_hp = self.normal_hp


class Fighter(Pokemon):
    def __init__(self, pokemon_trainer_):
        super().__init__(pokemon_trainer_)
        self.normal_power += 3
        self.current_power = self.normal_power
    
    
    def attack(self, enemy):
        super_power = randint(1, 3)
        self.current_power += super_power
        result = super().attack(enemy)
        self.current_power -= self.normal_power
        return result + f"Боец применил супер-атаку силой: {super_power}"