rawHours = input("Enter Hours: ")
rawRate = input("Enter Rate: ")

try:
    hours = float(rawHours)
    rate = float(rawRate)
except ValueError:
    print("Error, wrong input format!")
    quit()

if hours <= 40:
    print("Normal Time")
    print("Pay:", hours * rate)
else:
    restHours = hours - 40

    print("Overtime")
    print("Pay:", 40 * rate + (restHours * rate * 1.5))
