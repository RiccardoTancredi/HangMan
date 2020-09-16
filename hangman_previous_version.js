function word(parola){
    let tratto = "_ ";
    let trattini = tratto.repeat(parola.length);
    return trattini;
}
function continue_sostitution(original_parola, modified_parola, letter, index){
    let line = modified_parola.slice(0, Number(index));
    line += letter;
    line += modified_parola.slice(index+1, modified_parola.length);
    return line;
}

function initial_sostitution(original_parola, modified_parola, letter, index){
    if (index > 0) {
        index *= 2
    }
    if (modified_parola === ""){
        let line = word(original_parola);
        let line2 = line.slice(0,Number(index));
        line2 += letter;
        line2 += line.slice(index+1,line.length);
        return line2  
    }  
    else{
        return continue_sostitution(original_parola, modified_parola, letter, index);       
    }
}
function life(i){
    console.log("Hai ancora: ", 6-i,"vite");
    lives += 1;
    return i;
}

function guess(letter, parola, modified_parola = ""){
    if (parola.indexOf(letter) > - 1){
        let j = parola.replace(letter, "").length;
        // console.log("ci sono ", j, "lettere inserite");
        let paroletta = parola;
        if (j > 1){
            k = 0;
            p = 0;
            while (k < j){
                let indice = paroletta.search(letter);
                let indici = (indice+p);
                modified_parola = initial_sostitution(parola, modified_parola, letter, indici)
                p += indice+1
                paroletta = parola.slice(p,parola.length);
                k += 1;
            }
            return modified_parola;
        }
        else if (j === 1){
            let indici = paroletta.search(letter);
            modified_parola = initial_sostitution(parola, modified_parola, letter, indici);
            return modified_parola;
        }
    }
}
let parola = prompt("Inserisci la parola senza farti vedere: ");
parola = parola.toLowerCase();
let q = 0;
while (q < 11 ){
    console.log("*".repeat(q));
    q += 1;
}
let u = 9;
while (u >= 0) {
    console.log("*".repeat(u));
    u -= 1;
}
let j = 0;
let h = word(parola);
let tentativo = "";
let finale = "";
if (parola.indexOf(" " > -1)){
    tentativo = guess(" ",parola, tentativo);
    console.log(tentativo);
}
else{
    console.log(h);
}
let y = 0; 
while (y < parola.length){
    finale += parola[y];
    finale += " ";
    y += 1
}
let inserted_letters = [];
while (j < 6){
    let a = prompt("Inserisci una lettera:");
    if (a === "") a = prompt("Non hai inserito nulla, ritenta:");
    a = a[0].toLowerCase();
    if (tentativo !== "") {
        h = tentativo
    }
    if (parola.indexOf(a) > - 1){
        tentativo = guess(a,parola, tentativo);
        console.log(tentativo);
        life(j);
    }
    else{
        console.log("Hai perso una vita");
        console.log(h);
        j +=1;
        life(j);
    }
    if (inserted_letters.includes(a)){
        console.log("Hai già inserito questa lettere. Non ti distrarre, hai perso una vita");
        console.log(tentativo);
        j +=1;
        life(j);
    }
    inserted_letters.push(a);
    if (tentativo === finale){
        console.log("Hai indovito la parola,", finale ,"\n HAI VINTO!!!");
        break;
    }
    if (j === 6){
        console.log("Hai perso. La parola era: ", finale);
        break;
    }
}