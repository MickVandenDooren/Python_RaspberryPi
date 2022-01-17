from sense_hat import SenseHat
from time import sleep
from random import randint
from threading import Thread

sense = SenseHat()
sense.clear()

red = (255,0, 0)
black=(0,0,0)
blue = (0,0,255)
yellow=(255,255,0)
delay_decrease = 0.02







def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

def gen_pipes(matrix):
    for row in matrix:
        row[-1] = red
    gap = randint(1,6)
    matrix[gap][-1] = black
    matrix[gap - 1][-1] = black
    matrix[gap + 1][-1] = black
    return matrix

def move_pipes(matrix):
    
    
    
    
    for row in matrix:
        for i in range(7):
            row[i] = row[i+1]
        row[-1]=black
    return matrix

def draw_astronaut(event):
    global x
    global y
    global score
    global game_over
    
    sense.set_pixel(x,y, black)
    
    if event.action=="pressed":
        if event.direction=="up" and y>0 and game_over == False:
            y -=1
        elif event.direction == "down" and y<7 and game_over == False:
            y +=1
        elif event.direction == "middle" and score > 0:
            score = 0
    sense.set_pixel(x,y,yellow)
    
def check_collision(matrix):
    global game_over
    if matrix[y][x] == red:
        game_over = True
        return True
    else:
        return False

x= 0
y= 0
score = 0
game_delay = 2
game_over = False

sense.stick.direction_any = draw_astronaut

while True:
    matrix=[[black for column in range(8)] for row in range(8)]
    game_delay = 1
    game_over = False
    
    while True:
        matrix = gen_pipes(matrix)
        if check_collision(matrix):
            sleep(1)
            break
        
        for i in range(3):
            matrix = move_pipes(matrix)
            sense.set_pixels(flatten(matrix))
            sense.set_pixel(x,y,yellow)
            if check_collision(matrix):
                sleep(1)
                break
            
            if i == 2:
                score +=1
                game_delay -= delay_decrease
                if game_delay < 0.2:
                    game_delay = 0.2
            sleep(game_delay)
        
        
        
        
        
    while score:
        sense.show_message("Score:"+str(score))
        