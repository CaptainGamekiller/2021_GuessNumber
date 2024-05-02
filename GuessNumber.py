# One .py =  one module; multiple .py = one Package
import random
start = input('Please determine the number range start from: ')
end = input('Please determine the number range end to: ')
start = int(start)
end = int(end)

r = random.randint(start,end) # random integer，include 1 and 100
count = 0
while True:
    count += 1
    num = input('Please guess an integer number: ')
    num = int(num)
    if num == r:
        print('Correct!')
        break
    elif num < r:
        print('Your number is less than answer!')
    elif num > r:
        print('Your number is larger than answer!')
    print('You already guess', count , "time(s).")
