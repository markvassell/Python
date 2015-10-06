#Mark Vassell
#randwrite.py assignment

#This program takes a numeric input from a user to determine how many random
#number should be written to a file. It then write the specified amount of
#random numbers to that file.

import random

file_name = 'random_numbers.txt'

while (True):
    try:
        #Take input from the user
        input_number = int(input("How many random numbers would you like to generate? "))
        #checks if the input is a positive value and not zero
        if (input_number <= 0):
            print("Please enter a number that is greater than zero.")
            continue
        break
    except ValueError:
        #throws an error if the value is not numeric
        print("Please only input numeric values")

try:
    #opens a file to write to 
    random_num_file = open(file_name, "w")
    #writes random numbers to file base on the user input
    for i in range (input_number):
        random_num_file.write(str(random.randint(1,999)) + "\n")
    #closes the file
    random_num_file.close()
    print("The random numbers were successfully written to the file!")
#checks if there was an error with the file    
except:
    print("An error occured while trying to write the random numbers to", file_name)
