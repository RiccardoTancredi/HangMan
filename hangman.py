def word(parola:str):
    tratto = "_ "
    trattini = tratto*len(parola) 
    print(trattini)
    return trattini
c = word("cane")
#print(c)
def sostitution(parola:str, letter:str, index:int):
    line = word(parola)
    line[index] = letter
    print(line)
    return line

def life():
    pass

def guess(letter:str, parola:str):
    if letter in parola:
        #a = word(parola)
        j = 0
        while j < parola.count(letter):
            indice = parola.index(letter)
        d = sostitution(parola, letter, indice)
        return d

a = guess("c", "cane") 