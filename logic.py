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
    
    
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"
    
    
    # Метод класса для получения картинки покемона
    def show_front_img(self):
        return self.front_img
    
    
    def show_back_img(self):
        return self.back_img
