from random import *
a=randint(1,100)
guess=0
print('HELLO!')
print('Try to guess my number 1-100!')
c=int(input('Enter your number: '))
guess+=1
while c!=a:
    if a>c:
        print('My number is bigger than yours.')
    elif a<c:
        print('My number is lower than yours.')
    c=int(input('Enter your number: '))
    guess+=1
print('CORRECT!')
print('Tries: '+str(guess))
