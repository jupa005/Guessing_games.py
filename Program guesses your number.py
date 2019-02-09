from random import *
print('HELLO! WELCOME TO GUESSING GAME!')
print('Imagine one number 1-100 and i will try to guess it')
print('If your number is lower than my guess, press 1')
print('If your number is higher than my guess, press 2')
print('If I hit your number, press 3')
mini=1
maks=100
av=50
guess=0
c=randint(mini,maks)
a=int(input('Is your number '+str(c)+'?'))

guess+=1
while a!=3:
    guess+=1
    if a==1:
        maks=c-1
        c=randint(mini,maks)
    elif a==2:
        mini=c+1
        c=randint(mini,maks)
    a=int(input('Is your number '+str(c)+'?'))
    

print('I needed '+str(guess)+" tries to guess your number! ")
    
    
    
