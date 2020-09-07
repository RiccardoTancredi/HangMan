from p5 import *

def setup():
    size(700, 700)
    fill(255)
    f = create_font("Roboto.ttf", 16)
    text_font(f, 36)
    no_loop()
def word(parola:str):
    tratto = "_ "
    trattini = tratto*len(parola) 
    return trattini

def continue_sostitution(original_parola:str, modified_parola:str, letter:str, index:int):
    line = modified_parola[:index]
    line += letter
    line += modified_parola[index+1:]
    return line

def initial_sostitution(original_parola:str, modified_parola:str, letter:str, index:int):
    if index > 0:
        index *= 2
    if modified_parola == "":
        line = word(original_parola)
        line2 = line[:index]
        line2 += letter
        line2 += line[index+1:]
        return line2    
    else:
        return continue_sostitution(original_parola, modified_parola, letter, index)       
    
def life(i:int):
    fill(255)
    f = create_font("Roboto.ttf", 16)
    text_font(f, 36)
    text(f"Hai ancora: {6-i} vite", (50, 510))
    redraw()
    return i

def guess(letter:str, parola:str, modified_parola = ""):
    if letter in parola:
        j = parola.count(letter)
        paroletta = str(parola)
        if j > 1:
            k = 0
            p = 0
            while k < j:
                indice = paroletta.find(letter)
                indici = (indice+p)
                modified_parola = str(initial_sostitution(parola, modified_parola, letter, indici))
                p += indice+1
                paroletta = str(parola[p:])
                k += 1
            return modified_parola
        elif j == 1:
            indici = paroletta.find(letter)
            modified_parola = str(initial_sostitution(parola, modified_parola, letter, indici))
            return modified_parola

parola = input("Inserisci la parola senza farti vedere: ")
parola = parola.lower()
for i in range(11):
    print("*"*i)
for i in range(9,0,-1):
    print("*"*i)
j = 0
h = word(parola)
tentativo = ""
finale = ""
if " " in parola:
    tentativo = guess(" ",parola, tentativo)
    fill(255)
    f = create_font("Roboto.ttf", 16)
    text_font(f, 36)
    text(tentativo, (50, 510))
    redraw()
else:
    fill(255)
    f = create_font("Roboto.ttf", 16)
    text_font(f, 36)
    text(h, (50, 510))
    redraw()
for i in range(len(parola)):
    finale += parola[i]
    finale += " "
inserted_letters = []

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
    # a = input("Scrivi qualcosa ")
    # text(a, (50, 510))
    circle(350, 120, 40) # testa
    line((350, 120), (350, 350)) #body
    line((350, 170), (300, 230)) #left arm
    line((350, 170), (400, 230)) #right arm
    line((350, 350), (300, 410)) #left leg
    line((350, 350), (400, 410)) #right leg
    #hang_man = [circle(350, 120, 40), line((350, 120), (350, 350)), line((350, 170), (300, 230)), line((350, 170), (400, 230)), line((350, 350), (300, 410)), line((350, 350), (400, 410))]
run()
while j < 6:
    a = input("Inserisci una lettera:")
    if a == "": 
        a = input("Non hai inserito nulla, ritenta:")
    a = a[0].lower()
    if tentativo != "":
        h = str(tentativo)
    if a in parola:
        tentativo = guess(a,parola, tentativo)
        fill(255)
        f = create_font("Roboto.ttf", 16)
        text_font(f, 36)
        text(tentativo, (50, 510))
        redraw()
        life(j)
    else:
        fill(255)
        f = create_font("Roboto.ttf", 16)
        text_font(f, 36)
        text("Hai perso una vita", (50, 510))
        redraw()
        text(h, (50, 510))
        redraw
        j +=1
        life(j)
    if a in inserted_letters:
        fill(255)
        f = create_font("Roboto.ttf", 16)
        text_font(f, 36)
        text("Hai già inserito questa lettere. Non ti distrarre, hai perso una vita", (50, 510))
        redraw()
        text(tentativo, (50, 510))
        redraw()
        j +=1
        life(j)
    inserted_letters.append(a)
    if tentativo == finale:
        fill(255)
        f = create_font("Roboto.ttf", 16)
        text_font(f, 36)
        text(f"Hai indovito la parola, {finale} \n HAI VINTO!!!", (50, 510))
        redraw()
        break
    if j == 6:
        fill(255)
        f = create_font("Roboto.ttf", 16)
        text_font(f, 36)
        text(f"Hai perso. La parola era: {finale}", (50, 510))
        redraw()
        break
#ToDo: create a list with the entire body and the hangman and put it in the life() function... 
#ToDo: review the entire while loop of the programm and introuduce a fuction to write on p5