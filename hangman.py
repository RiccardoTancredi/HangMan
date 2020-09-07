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
    print("Hai ancora: ", 6-i,"vite")
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
    print(tentativo)
else:
    print(h)
for i in range(len(parola)):
    finale += parola[i]
    finale += " "
inserted_letters = []
while j < 6:
    a = input("Inserisci una lettera:")
    if a == "": 
        a = input("Non hai inserito nulla, ritenta:")
    a = a[0].lower()
    if tentativo != "":
        h = str(tentativo)
    if a in parola:
        tentativo = guess(a,parola, tentativo)
        print(tentativo)
        life(j)
    else:
        print("Hai perso una vita")
        print(h)
        j +=1
        life(j)
    if a in inserted_letters:
        print("Hai già inserito questa lettere. Non ti distrarre, hai perso una vita")
        print(tentativo)
        j +=1
        life(j)
    inserted_letters.append(a)
    if tentativo == finale:
        print("Hai indovito la parola,", finale ,"\n HAI VINTO!!!")
        break
    if j == 6:
        print("Hai perso. La parola era: ", finale)
        break