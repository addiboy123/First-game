# Importing Stuff
from pygame import *
from pygame.time import Clock
from time import sleep
init()

# Constants
WD,HT=1000,700
FPS=60
MAX_MIS=3
VEL=5
MIS_VEL=6
RED_HIT=USEREVENT+1 #Defining my own user-event
YELLOW_HIT=+USEREVENT+2 #Defining my own user-event

# Space & Spaceship (images)
SPACE=transform.scale(
image.load('F:\Python\My Python projects\Games\Assets\Space_purple.jpg'),(WD,HT))
icon_=transform.rotate(transform.scale(
image.load('F:\Python\My Python projects\Games\Assets\spaceship_red.png'),(32,32)),180)

spaceship__yellow=transform.rotate(transform.scale(
image.load('F:\Python\My Python projects\Games\Assets\spaceship_yellow.png'),(55,40)),270)

spaceship__red=transform.rotate(transform.scale(
image.load('F:\Python\My Python projects\Games\Assets\spaceship_red.png'),(55,40)),90)

red=Rect((WD/4)-(55/2),(HT/2)-20,55,40)
yellow=Rect(3*(WD/4)-(55/2),(HT/2)-20,55,40)

BORDER=Rect((WD//2)-5,0,10,HT)

# Sound & Music
mixer.music.load('F:\Python\My Python projects\Games\Assets\cornfield_chase.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)
fire_sound=mixer.Sound('F:\Python\My Python projects\Games\Assets\Gun+Silencer.mp3')
hit_sound=mixer.Sound('F:\Python\My Python projects\Games\Assets\Grenade+1.mp3')
fire_sound.set_volume(0.75)
hit_sound.set_volume(0.75)

#font
health_f=font.Font('freesansbold.ttf', 40)
play_again=font.Font('freesansbold.ttf', 20)
winner_f=font.Font('freesansbold.ttf', 100)

#Missile (images)
missile_r=transform.rotate(transform.scale(
image.load('F:\Python\My Python projects\Games\Assets\missile.png'),(32,32)),-45)
missile_y=transform.rotate(transform.scale(
image.load('F:\Python\My Python projects\Games\Assets\missile.png'),(32,32)),135)

# Screen
screen=display.set_mode((WD,HT))
display.set_caption('War Spaceship')
display.set_icon(icon_)

# Defining value function which is required for looping the game
def value():
    global health_r,health_y,l_r, l_y,l_ri,l_yi

    health_r=10
    health_y=10
    l_r=[]
    l_y=[]
    l_ri=[]
    l_yi=[]
    for i in range(MAX_MIS):
        l_ri.append(missile_r)
        l_yi.append(missile_y)

value()

# Defining all other imp functions
def win_display(red,yellow,health_r,health_y):
    screen.blit(SPACE,(0,0))
    red_H_text=health_f.render('Health : '+str(health_r),True,(255,255,255))
    yellow_H_text=health_f.render('Health : '+str(health_y),True,(255,255,255))
    play_again_text=play_again.render('Press Enter to Play Again',True,(255,255,255))
    
    winner_r=winner_f.render('RED WINS!!',1,(255,255,255))
    winner_y=winner_f.render('YELLOW WINS!!',1,(255,255,255))
    screen.blit(SPACE,(0,0))
    
    draw.rect(screen,(0,0,0),BORDER)
    screen.blit(spaceship__red,(red.x,red.y)) #(WD/4)-(55/2),(HT/2)-20
    screen.blit(spaceship__yellow,(yellow.x,yellow.y)) #3*(WD/4)-(55/2),(HT/2)-20
    
    screen.blit(yellow_H_text,(WD/2+10,10))
    screen.blit(red_H_text,(10,10))
    

    for i in range(len(l_r)):
        screen.blit(l_ri[i],(l_r[i].x,l_r[i].y))
    for aa in range(len(l_y)):
        screen.blit(l_yi[aa],(l_y[aa].x,l_y[aa].y)) 
    if health_r==0:
        screen.blit(winner_y,((WD/2)-(winner_y.get_width()/2),HT/2-10))
        screen .blit(play_again_text,((WD/2)-(play_again_text.get_width()/2),HT/2+90))
    elif health_y==0:
        screen.blit(winner_r,((WD/2)-(winner_r.get_width()/2),HT/2-10))
        screen .blit(play_again_text,((WD/2)-(play_again_text.get_width()/2),HT/2+90))

def spaceship_movement(key_,health_r,health_y):
    global red,yellow
    if health_r!=0 and health_y!=0:
         #red
        if key_[K_a] and red.x>2:   #left
            red.x-=VEL
        if key_[K_d] and red.x<(WD/2)-50:   #Right
            red.x+=VEL 
        if key_[K_w] and red.y>0:   #Up
            red.y-=VEL
        if key_[K_s] and red.y<HT-55:   #Down
            red.y+=VEL
        #yellow
        if key_[K_LEFT] and yellow.x>(WD/2)+10:    #left
            yellow.x-=VEL
        if key_[K_RIGHT] and yellow.x<WD-48:   #Right
            yellow.x+=VEL
        if key_[K_UP] and yellow.y>0:   #Up
            yellow.y-=VEL
        if key_[K_DOWN] and yellow.y<HT-55:   #Down
            yellow.y+=VEL

def Missile():
    for j in l_r:
        j.x+=MIS_VEL
        if j.x >WD:
            l_r.remove(j)
        elif yellow.colliderect(j):
            l_r.remove(j)
            hit_sound.play()
            event.post(event.Event(YELLOW_HIT)) #Creating ur own event and posting it
    
    for y in l_y:
        y.x-=MIS_VEL
        if y.x <0:
            l_y.remove(y)
        elif red.colliderect(y):
            l_y.remove(y)
            hit_sound.play()
            event.post(event.Event(RED_HIT)) #Creating ur own event and posting it

# Defining the main function
def main():
    alpha=time.Clock() #using time so the looping doesn't exceed 60 fps
    global health_r,health_y
    flag_=True
    while flag_:
        alpha.tick(FPS)  #using time so the looping doesn't exceed 60 fps
        for i in event.get(): #Looping through the events
            if i.type==QUIT:
                flag_=False
                quit()
                
            if i.type == KEYDOWN: # imp syntax  for controlling movement
                if health_r==0 or health_y==0:
                    if i.key==K_KP_ENTER:
                        value() 
                    break
                if i.key == K_LCTRL and len(l_r)<MAX_MIS:
                    missile_red=Rect(red.x,red.y,32,32)
                    l_r.append(missile_red)
                    fire_sound.play()
                if i.key==K_RCTRL and len(l_y)<MAX_MIS:
                    missile_yellow=Rect(yellow.x,yellow.y,32,32)
                    l_y.append(missile_yellow)
                    fire_sound.play()
                
            if i.type==RED_HIT and health_r!=0:
                health_r-=1  
            if i.type==YELLOW_HIT and health_y!=0:
                health_y-=1    
        
        win_display(red,yellow,health_r,health_y)
        key_=key.get_pressed() # Another way of controlling movement
        spaceship_movement(key_,health_r,health_y)
        Missile()
        display.update()
        
        

if __name__=="__main__": # calling the main function
    main()