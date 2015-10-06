print("Object Position Calculator!\n")
#User input section

while True:

    try:
        initial_position_x = float(input("Please enter the intial position of the object (meters): "))

    except ValueError:
        print "The string you entered needs to be a numeric value \n"
        continue
    else:
        break



initial_velocity = float(input("\nPlease enter the intial velocity of the object (m/s): "))

acceleration = float(input("\nPlease enter the acceleration of the object (m/s^2): "))

time = float(input("\nPlease enter how long was the object in motion (time in seconds): "))
#calculate final position based on user inputs
final_position = initial_position_x + initial_velocity * time + 0.5 * acceleration * time**2
print "\nThe final position of the object is: %.2f meters" % final_position
