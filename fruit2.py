'''*******************************
น.ส.ธรรณศร เมตตา
6206021611125
Sec B Chapter 2
******************************'''
import pgzrun
import random

WIDTH = 640
HEIGHT = 480
apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')

def draw():
    screen.fill((100,200,200))
    apple.draw()
    orange.draw()
    pineapple.draw()

def place_apple():
    apple.x = random.randint(0,640)
    apple.y = random.randint(0,0)

def place_orange():
    orange.x = random.randint(0,640)
    orange.y = random.randint(0,0)

def place_pineapple():
    pineapple.x = random.randint(0,640)
    pineapple.y = random.randint(0,0)
    
def update():
    if apple.y < HEIGHT:
        apple.y +=1
    else :
        apple.x = random.randint(0,640)
        apple.y = random.randint(0,0)
    if orange.y < HEIGHT:
        orange.y +=1
    else :
        orange.x = random.randint(0,640)
        orange.y = random.randint(0,0)
    if pineapple.y < HEIGHT:
        pineapple.y +=1
    else :
        pineapple.x = random.randint(0,640)
        pineapple.y = random.randint(0,0)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        place_apple()
        print('Good Shot!')
    elif orange.collidepoint(pos):
        place_orange()
        print('Good Shot!')
    elif pineapple.collidepoint(pos):
        place_pineapple()
        print('Good Shot!')
    else :
        print('You Missed!')

place_gewe()
place_orange()
pgzrun.go()
