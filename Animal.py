# Program: Animal.py
# This program defines the Animal class

import random


class Animal:
    # Define what happens when a new animal object is created
    def __init__(self, animal_type, animal_name):
        self.__animal_type = animal_type
        self.__name = animal_name

        # Pick a number between 1 and 3
        random_number = random.randint(1, 3)

        # Set the animal's mood based on the random number
        if random_number == 1:
            self.__mood = "happy"
        elif random_number == 2:
            self.__mood = "hungry"           
        elif random_number == 3:
            self.__mood = "sleepy"
        

    # Return the animal's type
    def get_animal_type(self):
        return self.__animal_type

    # Return the animal's name
    def get_name(self):
        return self.__name

    # Return the animal's mood
    def check_mood(self):
        return self.__mood


class Mammal(Animal):
    # Define what happens when a new bird object is created
    def __init__(self, animal_type, animal_name, hair_color):
        # Call Animal's __init__
        Animal.__init__(self, animal_type, animal_name)
        
        # Initialize the __hair_color attribute
        self.__hair_color = hair_color
    
    
    # Return the mammal's leg count
    def get_hair_color(self):
        return self.__hair_color


class Bird(Animal):
    # Define what happens when a new bird object is created
    def __init__(self, animal_type, animal_name, can_fly):
        # Call Animal's __init__
        Animal.__init__(self, animal_type, animal_name)
        
        # Initialize the __can_fly attribute
        self.__can_fly = can_fly
    
    
    # Return if the bird can fly
    def get_can_fly(self):
        return self.__can_fly
