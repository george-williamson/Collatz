import sys

steps = 0


def collatz(number):

    global steps

    if number <= 0:
        print('The number you have entered is not greater than 1.')
        sys.exit()
    if number == 1:
        print('Amount of steps: ' + str(steps))
        print('Collatz sequence is finished.')
    elif number % 2 == 0:
        steps += 1
        print(int(number/2))
        collatz(number/2)
    else:
        steps += 1
        print(int(3*number + 1))
        collatz(3*number + 1)


print('Enter an integer greater than 1.')


try:
    collatz(int(input()))
except ValueError:
    print('Please enter an integer.')
