
count = 0
total = 0

while True:
    sval = input("Gibt eine Nummer ein: ")

    if sval == "done":
        print(count, total, total / count);
        break

    try:
        fval = float(sval)
    except ValueError:
        print("Invalid input")
        continue

    count = count + 1
    total = total + fval
