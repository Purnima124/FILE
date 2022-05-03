with open("file.txt", "w") as file:
    data=file.readlines()
    for line in data:
        word = line.split()
        print (word)