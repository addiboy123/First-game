
#  ADITYA's GAMING BOT 


from time import sleep
from random import randrange
sleep (2)
print('''AI-
Hey user, your personal AI gaming bot is here
 ''')
sleep(2)
print('Do you want to play a Game? (Yes or No)')
while True:
    a=input()
    a=a.title()
    if a=='Yes':
        for i in range(1,6):
            print('.'*i)
            sleep(1)
        print("""
        AI- 
        Hey user let's play a game
        """)
        sleep(1)
        print('''rules are pretty simple
        ''')
        sleep(1)
        print('''I choose a no. from 1 to 1000 
        You choose a no. from 1 to 1000
        ''')
        sleep(1)
        print('''If they match you win
        if they dont match you lose
        ''') 
        sleep(1)
        print('Good luck')
        while True:
            b=input('    Are you ready? (yes or no)\n')
            b=b.title()
            if b=='Yes':
                    while True:
                        g=input('''Select a level-
                    [Easy{20 tries}, Normal{15 tries} or Hard{10 tries}]
                    ''')
                        g=g.title()
                        if g=='Easy' or g=='Normal' or g=='Hard':
                            break
                        else:
                            print('Enter Easy, Normal or Hard idiot')
                    print('Game Starting in...')
                    sleep(1)
                    for j in range(5,0,-1):
                        print(j)
                        sleep(1)
                    print('Begin...')
                    n=randrange(1000)
                    c=1
                    while True:
                        
                        sleep(0.5)
                        print('your try no.',c)
                        try:
                            d=int(input('Enter a no. '))
                        except ValueError:
                            sleep(0.25)
                            print('''Enter a no. dumbass
                            ''')
                            continue
                        sleep(0.25)
                        if d==n:
                            print('''
                            YOU WIN ( ͡° ͜ʖ ͡°) !!!''')
                            break
                        elif d>1000 or d<0:
                            print('''
                            Enter a no. between 0 to 1000''')
                            continue
                        elif d>n:
                            print('''
                            Hint: SMALLER''')
                        elif d<n:
                            print('''
                            Hint: LARGER''')
                        if g=='Easy':
                            if c==20:
                                print('''20 tries over
                            YOU LOST
                            The no. was''',n)
                                sleep(1)
                                print('GAME OVER')
                                break
                        elif g=='Normal':
                            if c==15:
                                print('''10 tries over
                            YOU LOST
                            The no. was''',n)
                                sleep(1)
                                print('GAME OVER')
                                break
                        elif g=='Hard':
                            if c==10:
                                print('''5 tries over
                            YOU LOST
                            The no. was''',n)
                                sleep(1)
                                print('GAME OVER')
                                break
                        
                        c=c+1
                    f=0
                    while True:
                        e=input('Wanna Play again? (Yes or No)\n')
                        e=e.title()
                        if e=='No':
                            f=1
                            break
                        elif e=='Yes':
                            break
                        else:
                            print('Yes or No dumbass')     
                    if f==1:
                        break        
            elif b=='No':
                print('Then get ready dumbass')
            else:
                print('Yes or No dumbass')
        break
    elif a=='No':
        print('Then Go Away')
        break
    else:
        print('Yes or No- dumbass')
    
if a=='Yes':           
    print('''
    AI-
    Thanks for playing''')
    
 




