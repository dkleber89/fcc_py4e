filename = input("Enter a file name: ")

filehandle = open(filename)

for line in filehandle:
    print(line.rstrip().upper())
