import Animal, Zoo

def main():
    # Create a Zoo object
    zoo = Zoo.Zoo()
    
    # This program will loop until the user says to exit
    while True:
        
        # Print zoo options
        display_menu()

        # Ask for a choice
        while True:
            try:
                choice = int(input("What would you like to do? "))
                if choice < 1 or choice > 3:
                    print("Please select a valid option.\n")
                    continue
            except ValueError:
                print("Please enter a numeric value.\n")
            else:
                break

        # Add Animal
        if choice == 1:
            # Ask the user for the animal's type and name
            animal_type = input("\nWhat type of animal would you like to create? ")
            animal_name = input("What is the animal's name? ")
            print()

            # Create a new Animal object
            animal = Animal.Animal(animal_type, animal_name)

            # Add the Animal to the Zoo
            zoo.add_animal(animal)

        # View Animals
        elif choice == 2:
            zoo.show_animals()
            
        # Exit
        else:
            print("\nThank you for visiting the zoo!")
            break


# Function that displays the main options
def display_menu():
    print("Zoo Options")
    print("-----------")
    print("1. Add Animal")
    print("2. Show Animals")
    print("3. Exit")
    print()


# Cal main
main()
