from p5 import *

def setup():
    size(700, 700)
    no_loop()
    
def draw():
    background(0)
    fill(255)
    stroke(255)
    line((0, 500), (700, 500))
    line((50, 50), (50, 500))
    line((50,50), (350,50))
    line((350, 50), (350, 100))
    #Here the game // 6 total lives
    #now let's try to create the man, as the gamer loses lives
    fill(255)
    f = create_font("Roboto.ttf", 16)
    text_font(f, 36)
    a = input("Scrivi qualcosa ")
    text(a, (50, 510))
    circle(350, 120, 40) # testa
    line((350, 120), (350, 350)) #body
    line((350, 170), (300, 230)) #left arm
    line((350, 170), (400, 230)) #right arm
    line((350, 350), (300, 410)) #left leg
    line((350, 350), (400, 410)) #right leg
    #hang_man = [circle(350, 120, 40), line((350, 120), (350, 350)), line((350, 170), (300, 230)), line((350, 170), (400, 230)), line((350, 350), (300, 410)), line((350, 350), (400, 410))]
run()
#ToDo: create a list with the entire body and the hangman and put it in the life() function... 
#ToDo: review the entire while loop of the programm and introuduce a fuction to write on p5