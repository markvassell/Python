print("Happy numbers finder\nPlease enter 10 numbers")
print("Press return after each number")
#array that stores the users inputs
input_number = []

#this loop loads the user's ten integer inputs in the array
for i in range(10):
    while True:
        try:
            value = int(input( ))
            if (value < 0):
                print("Please only enter positive integer values")
                continue
            else:
                input_number.append(value)
                break
        except ValueError:
            print("Please only input positive numerical values.")
            continue

#function to add the values in an array together then return the total.
def adder (array):
    add = 0
    for i in array:
        add = add + i

    return add

#funtion that takes in an array and squares all the values in it.
#Returns an array with the new values in it
def sqr (array):
    new = []
    for i in array:
        new.append(i**2)
    return new
#Check if a value is already in an array
def found(digit, array):
    if not array:
        return digit
    for num in array:
        #print("num = {0} digit = {1}" .format(num,digit))
        if digit == num:
            return 1

    return digit
#takes a string and split it up into characters.
#Returns an array of characters 
def make_split(string):
    array = []
    splits = [int(i)for i in string]
    for c in splits:
        array.append(c)
    return array



for x in input_number:
    split_array = []
    num_array = []
    origin_value = x
    counter = 0
    if origin_value == 1:
        print ("happy {0}".format(counter))
        continue
    else:
        split_array = make_split(str(x))
        split_array = sqr(split_array)
        summed_value = adder(split_array)

        counter = 1;

    while True:
        if (summed_value == 1):
 
            print ("happy {0}".format(counter))
            break
        else:
            
            finder = found(summed_value, num_array)

            if (finder == 1):
                if origin_value < 10:
                    counter -= 1
                print("unhappy {0}".format(counter))
                break
            else:
                num_array.append(finder)
                split_array = make_split(str(summed_value))
                split_array = sqr(split_array)
                summed_value = adder(split_array)
        counter += 1
        continue





