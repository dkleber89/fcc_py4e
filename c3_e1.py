rawHours = input("Enter Hours: ")
rawRate = input("Enter Rate: ")

hours = float(rawHours)
rate = float(rawRate)

if hours <= 40:
    print("Normal Time")
    print("Pay:", hours * rate)
else:
    restHours = hours - 40

    print("Overtime")
    print("Pay:", 40 * rate + (restHours * rate * 1.5))
