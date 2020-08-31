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
    print("Hai ancora: ", 7-i,"vite")
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
for i in range(11):
    print("*"*i)
for i in range(9,0,-1):
    print("*"*i)
j = 0
h = word(parola)
print(h)
tentativo = ""
finale = ""
for i in range(len(parola)):
    finale += parola[i]
    finale += " "
while j < 7:
    a = input("Inserisci una lettera:")
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
    if tentativo == finale:
        print("Hai indovito la parola,", finale ,"hai vinto")
        break
    if j == 7:
        print("Hai perso. La parola era: ", finale)
        break