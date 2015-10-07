import math
print("This is test multiplication table: Still in progress")
file_name = "Multiples.txt"
try:
    #opens a file to write to
    mult_file = open(file_name, "w")
    while (True):
        try:
            inp_range = int(input("Please enter how many multiplication tables you would like to generate: "))
            if(inp_range <= 0):
                print("Please only enter numeric values that are greater than zero: ")
                continue
            break
        except ValueError:
            print("Plase only enter a numeric value")
            continue
    for i in range(1,inp_range+1):

        for j in range(1,inp_range+1):
            mult_file.write(str(i*j) + "\n")
        mult_file.write("\n")

    mult_file.close()
    print("The tables were successfully written to the file!")
except:
    print("An error occured while trying to write the random numbers to", file_name)





#used to find the range
#http://pythoncentral.io/pythons-range-function-explained/

#learned about for loops in python
#http://www.tutorialspoint.com/python/python_for_loop.htm

#errors and exceptions
#https://docs.python.org/2/tutorial/errors.html

#how to write to a file in python.
#http://learnpythonthehardway.org/book/ex16.html
