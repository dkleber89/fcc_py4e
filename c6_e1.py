baseString = "X-DSPAM-Confidence: 0.8475 "

spacePosition = baseString.find(":")
numberString = baseString[spacePosition + 1:]
number = float(numberString)

print(number)
