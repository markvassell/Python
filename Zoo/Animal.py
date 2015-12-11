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
