from p5 import *

def setup():
    size(700, 700)

def draw():
    background(0)
    fill(255)
    # rect_mode(CENTER)
    # rect((100, 100), 20, 100)
    # ellipse((100, 70), 60, 60)
    # ellipse((81, 70), 16, 32)
    # ellipse((119, 70), 16, 32)
    # line((90, 150), (80, 160))
    # line((110, 150), (120, 160))
    stroke(255)
    line((0, 500), (700, 500))
    line((50, 50), (50, 500))
    line((50,50), (350,50))
    line((350, 50), (350, 100))
    #Here the game // 6 total lives
    #now let's try to create the man, as the gamer loses lives
    circle(350, 120, 40) # testa
    line((350, 120), (350, 350)) #body
    line((350, 170), (300, 230)) #left arm
    line((350, 170), (400, 230)) #right arm
    line((350, 350), (300, 410)) #left leg
    line((350, 350), (400, 410)) #right leg
run()

#ToDo: create a list with the entire body ogìf the hangman and put it in the life() function... 
#ToDo: review the entire while loop of the programm and introuduce a fuction to write on p5