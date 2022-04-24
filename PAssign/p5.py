import sys
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not a valid number! Try again.")

print("Your number doubled is:", number * 2)

default_greeting = "Hello World!"
filename = "greeting.txt"


def askyesno(question):
    while True:
        answer = input(question + ' (y or n) ')
        if answer == 'Y' or answer == 'y':
            return True
        if answer == 'N' or answer == 'n':
            return False


def greet():
    with open(filename, 'r') as f:
        for line in f:
            print(line.rstrip('\n'))


try:
    greet()
except OSError:
    print("Cannot read '%s'!" % filename, file=sys.stderr)
    if askyesno("Would you like to create a default greeting file?"):
        with open(filename, 'w') as f:
            print(default_greeting, file=f)
        greet()





