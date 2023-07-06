#Just a thing I made for fun in my free time!

import os
import random
os.system('title Rigged Rock Paper Scissors')
os.system('cls')

r = input('Rock, Paper Or Scissors? ')

if r == 'Rock'.lower():
    o = 'Rock', 'Paper', 'Scissors'
    c = random.choice(o).lower()
    
    if r.lower() == 'rock':
        if c.lower() == 'scissors': #if the computer chooses scissors
            print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", you win!")
        if c.lower() == 'rock': #if the computer chooses rock
            print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", It's a draw..")
        if c.lower() == 'paper': #if the computer chooses paper
             print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", I win")

    if r.lower() == 'paper':
        if c.lower() == 'scissors': #if the computer chooses scissors
            print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", I win!")
        if c.lower() == 'rock': #if the computer chooses rock
            print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", you win!")
        if c.lower() == 'paper': #if the computer chooses paper
             print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", It's a draw..")

    if r.lower() == 'scissors':
        if c.lower() == 'scissors': #if the computer chooses scissors
            print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", It's a draw..")
        if c.lower() == 'rock': #if the computer chooses rock
            print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", I win!")
        if c.lower() == 'paper': #if the computer chooses paper
             print('You chose' + ' "' + r.lower() + '" ' + "and I chose " + '"' + c.lower() + '"' + ", you win!")

p = input('[ \033[1;32;40mY \033[1;37;40m| \033[1;31;40mN \033[1;37;40m] play again > ')

if p.lower() == 'no' or p.lower() == 'n':
    os.system('exit')
else:
    if p.lower() == 'yes' or p.lower() == 'y':
        os.system('cls')
        os.system('py ./play.py')
    
