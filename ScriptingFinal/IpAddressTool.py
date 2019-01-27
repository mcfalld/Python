from StudentIPAddress import StudentIPAddress
import sys
import time

count = 0
startingIp = StudentIPAddress()
endingIp = StudentIPAddress()
defaultStartingIp = "0.0.0.0"
defaultEndingIp = "255.255.255.255"

# starting = input("Please enter the starting ip address: ")
try:
    starting = input("Please enter the starting ip address: ")
    if starting is None or str(starting) == "":
        starting = defaultStartingIp
except SyntaxError:
    starting = defaultStartingIp
while not startingIp.startingValidIPAddress(starting):
    starting = input("Please enter a valid starting ip address \n(Should not contain letters or symbols \nand "
                     "Must have 3 decimal points): ")
    if starting is None or str(starting) == "":
        starting = defaultStartingIp
print(startingIp)
# ending = input("Please enter the ending ip address: ")
try:
    ending = input("Please enter the ending ip address: ")
    if ending is None or str(ending) == "":
        ending = defaultEndingIp
except SyntaxError:
    ending = defaultEndingIp
while not endingIp.endingValidIPAddress(ending):
    ending = input("Please enter a valid ending ip address \n(Should not contain letters or symbols \nand "
                   "must have 3 decimal points): ")
    if ending is None or str(ending) == "":
        ending = defaultEndingIp
print(endingIp)
# print(startingIp)
# print(endingIp)
# print("startingIp.DottedDecimalNotation: " + startingIp.DottedDecimalNotation())
# print("startingIp.__str__")
# print(startingIp)
# print("endingIp.DottedDecimalNotation: " + endingIp.DottedDecimalNotation())
# print("endingIp.__str__")
# print(startingIp.NextAddress())
# print(startingIp.NextAddress())
# print(startingIp + 222)
# print(startingIp.IsSmaller(endingIp))


f = open('LabIPAddresses.txt', 'w')
f.write(str(startingIp))
while startingIp.IsSmaller(endingIp):
    startingIp.NextAddress()
    f.write(str(startingIp))
    count += 1
    if count % 10 == 0:

        sys.stdout.write("\r%d ip's have been added to the list." % count)
        sys.stdout.flush()
        time.sleep(.01)
f.close()

# input()
