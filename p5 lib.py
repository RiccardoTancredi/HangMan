from p5 import *

lives = None
tentativo = None
finale = None
inserted_letters = None
parola = None
h = None


def word(parola: str):
    tratto = "_ "
    trattini = tratto*len(parola)
    return trattini


def continue_sostitution(original_parola: str, modified_parola: str, letter: str, index: int):
    line = modified_parola[:index]
    line += letter
    line += modified_parola[index+1:]
    return line


def initial_sostitution(original_parola: str, modified_parola: str, letter: str, index: int):
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


def life(i: int):
    global lives
    print("Hai ancora: ", 6-lives, "vite")
    return lives


def guess(letter: str, parola: str, modified_parola=""):
    if letter in parola:
        j = parola.count(letter)
        paroletta = str(parola)
        if j > 1:
            k = 0
            p = 0
            while k < j:
                indice = paroletta.find(letter)
                indici = (indice+p)
                modified_parola = str(initial_sostitution(
                    parola, modified_parola, letter, indici))
                p += indice+1
                paroletta = str(parola[p:])
                k += 1
            return modified_parola
        elif j == 1:
            indici = paroletta.find(letter)
            modified_parola = str(initial_sostitution(
                parola, modified_parola, letter, indici))
            return modified_parola


def init():
    global lives, tentativo, finale, inserted_letters, parola, h
    lives = 0
    parola = input("Inserisci la parola senza farti vedere: ")
    parola = parola.lower()
    for i in range(11):
        print("*"*i)
    for i in range(9, 0, -1):
        print("*"*i)
    h = word(parola)
    tentativo = ""
    finale = ""
    if " " in parola:
        tentativo = guess(" ", parola, tentativo)
        print(tentativo)
    else:
        print(h)
    for i in range(len(parola)):
        finale += parola[i]
        finale += " "
    inserted_letters = []


def setup():
    size(700, 700)
    fill(255)
    f = create_font("Roboto.ttf", 16)
    text_font(f, 36)
    no_loop()
    init()


def draw():
    # game graphics
    has_to_redraw = True
    global lives, tentativo, finale, inserted_letters, parola, h
    if has_to_redraw:
        if lives == 0:
            background(0)
            fill(255)
            stroke(255)
            line((0, 500), (700, 500))
            line((50, 50), (50, 500))
            line((50, 50), (350, 50))
            line((350, 50), (350, 100))
        elif lives == 1:
            circle(350, 120, 40)  # head
        elif lives == 2:
            line((350, 120), (350, 350))  # body
        elif lives == 3:
            line((350, 170), (300, 230))  # left arm
        elif lives == 4:
            line((350, 170), (400, 230))  # right arm
        elif lives == 5:
            line((350, 350), (300, 410))  # left leg
        elif lives == 6:
            line((350, 350), (400, 410))  # right leg
        has_to_redraw = False
    # game logic
    a = input("Inserisci una lettera:")
    print("ciao")
    if a == "":
        a = input("Non hai inserito nulla, ritenta:")
    a = a[0].lower()
    if tentativo != "":
        h = str(tentativo)
    if a in parola:
        tentativo = guess(a, parola, tentativo)
        print(tentativo)
        life(lives)
    else:
        print("Hai perso una vita")
        print(h)
        lives += 1
        has_to_redraw = True
        life(lives)
    if a in inserted_letters:
        print("Hai già inserito questa lettere. Non ti distrarre, hai perso una vita")
        print(tentativo)
        lives += 1
        has_to_redraw = True
        life(lives)
    inserted_letters.append(a)
    if tentativo == finale:
        print("Hai indovito la parola,", finale, "\n HAI VINTO!!!")
        # break
    if lives == 6:
        print("Hai perso. La parola era: ", finale)
        # break
    if lives <= 6 and tentativo != finale:
        draw()

    # Here the game // 6 total lives
    #hang_man = [circle(350, 120, 40), line((350, 120), (350, 350)), line((350, 170), (300, 230)), line((350, 170), (400, 230)), line((350, 350), (300, 410)), line((350, 350), (400, 410))]
run()
# ToDo: create a list with the entire body and the hangman and put it in the life() function...
# ToDo: review the entire while loop of the programm and introuduce a fuction to write on p5
