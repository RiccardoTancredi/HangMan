let lives = 0;

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
    // lives += 1;
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
if (parola.indexOf(" ") > -1){
    tentativo = guess(" ",parola, tentativo);
    console.log(tentativo);
}
else{
    console.log(word(parola));
}
let y = 0; 
while (y < parola.length){
    finale += parola[y];
    finale += " ";
    y += 1
}

function setup(){
    background(0);
    createCanvas(700, 700);
    stroke(255);  
    line(0, height/2, width, height/2);
    line(50, 50, 50, height/2);
    line(50, 50, width/2, 50);
    line(width/2, 50, width/2, 100);
}


let inserted_letters = [];



function draw(){
    background(0);
    //let hang_man = [circle(width/2, 120, 40), line(width/2, 120, width/2, height/2-100), line(width/2, 170, 300, 230), line(width/2, 170, 400, 230), line(width/2, height/2 - 100, 300, 330), line(width/2, height/2 - 100, 400, 330)];
    stroke(255);
    strokeWeight(2);

    // Start
    stroke(255);  
    line(0, height/2, width, height/2);
    line(50, 50, 50, height/2);
    line(50, 50, width/2, 50);
    line(width/2, 50, width/2, 100);
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
        console.log("Hai già inserito questa lettera. Non ti distrarre, hai perso una vita");
        console.log(tentativo);
        j +=1;
        circle(500,500,50);
        life(j);
    }
    inserted_letters.push(a);
    if (tentativo === finale){
        console.log("Hai indovito la parola,", finale ,"\n HAI VINTO!!!");
        //break;
        noLoop();
    }
    if (j === 1){
        circle(width/2, 120, 40);
    }
    else if (j === 2){
        circle(width/2, 120, 40);
        line(width/2, 120, width/2, height/2-100);
    }
    else if (j === 3){
        circle(width/2, 120, 40);
        line(width/2, 120, width/2, height/2-100);
        line(width/2, 170, 300, 230);
    }
    else if (j === 4){
        circle(width/2, 120, 40);
        line(width/2, 120, width/2, height/2-100);
        line(width/2, 170, 300, 230);
        line(width/2, 170, 400, 230);
    }
    else if (j === 5){
        circle(width/2, 120, 40);
        line(width/2, 120, width/2, height/2-100);
        line(width/2, 170, 300, 230);
        line(width/2, 170, 400, 230);
        line(width/2, height/2 - 100, 300, 330)
    }
    else if (j === 6){
        circle(width/2, 120, 40);
        line(width/2, 120, width/2, height/2-100);
        line(width/2, 170, 300, 230);
        line(width/2, 170, 400, 230);
        line(width/2, height/2 - 100, 300, 330)
        line(width/2, height/2 - 100, 400, 330);
        console.log("Hai perso. La parola era: ", finale);
        // break;
        noLoop();
    }
}

