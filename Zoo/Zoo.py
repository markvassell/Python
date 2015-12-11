# Zoo.py
# Defines the Zoo class

class Zoo:
    def __init__(self):
        # Create an empty list for the Animal objects
        self.__animals = []

    def add_animal(self, animal):
        # Append the Animal object to the __animals list
        self.__animals.append(animal)

    def show_animals(self):
        # Print a header
        print("\nAnimal List")
        print("-----------")
        
        # Check for Animal objects
        # If there are none, print a message
        if len(self.__animals) < 1:
            print("There are no animals in your zoo!")

        # Otherwise, print their names, types, and moods
        else:
            # Loop through the list
            for animal in self.__animals:
                # Use accessor methods to get each Animal object's information
                animal_name = animal.get_name()
                animal_type = animal.get_animal_type()
                animal_mood = animal.check_mood()

                # Print the Animal object's information
                print(animal_name, "the", animal_type, "is", animal_mood)

        # Print an extra line
        print()
