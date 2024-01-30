from time import time

while True:
    line = input()

    milliseconds = int(time() * 1000)

    print(str(milliseconds) + " || " + line)
