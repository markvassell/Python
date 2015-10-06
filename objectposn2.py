print("Object Position Calculator!\n")
#User input section
loop = 'y'
#Checks if the user wants to run the program again.
while loop == 'y':
    #Checking if the user input is a numeric value and if not loop until it is
    while True:

        try:
            initial_position_x = float(input("Please enter the intial position of the object (meters): "))

        except ValueError:
            print ("\nThe initial position you entered needs to be a numeric value \n")
            continue
        else:
            break

    #Checking if the user input is a numeric value and if not loop until it is
    while True:
        try:
            initial_velocity = float(input("\nPlease enter the intial velocity of the object (m/s): "))
        except ValueError:
            print("\nThe initial velocity you entered needs to be a numeric value\n")
            continue
        else:
            break
    #Checking if the user input is a numeric value and if not loop until it is
    while True:
        try:
            acceleration = float(input("\nPlease enter the acceleration of the object (m/s^2): "))
        except ValueError:
            print("\nThe acceleration you entered need to be a numeric value\n")
            continue
        else:
            break
        
    #Checking if the user input is a numeric value and if not loop until it is
    while True:
        try:
            time = float(input("\nPlease enter how long was the object in motion (time in seconds): "))
            #check if time is negative and if it is request a new input from the user.
            if time < 0:
                print ("\nYou aren't allowed to have negative time.\n")
                continue
            else:
                break
        except ValueError:
            print("\n Only input numeric values for time \n")
            continue
        else:
            break

        
    #calculate final position based on user inputs
    final_position = initial_position_x + initial_velocity * time + 0.5 * acceleration * time**2
    print ("\nThe final position of the object is: %.2f meters\n\n" % final_position)

    loop = input("Would you like to run another calculation? type y for yes or anything else to quit: ")


