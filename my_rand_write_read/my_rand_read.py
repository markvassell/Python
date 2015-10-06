file_name = "random_numbers.txt"
counter = 0
try:
    file = open(file_name, "r")

    for numbers in file:
        counter += 1
        file_number = int(numbers)
        print(file_number)
    file.close()
    print("There are %d nmbers in the file" %counter)
except:
    print("There was an error while trying to read", file_name)


