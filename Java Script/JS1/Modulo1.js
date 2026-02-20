// Area de testes




/*
Variaveis 

let - Não funciona fora dos blocos
var - Funciona fora dos blocos

*/
{
let numero = 150;
console.log(numero);
}
/*
A maioria das coisas sõa bastante parecidas com python

sistemas de operadores
variaveris
redefinição

*/
{
let palavra_1 = "Esta é uma palavra ";
let numero_1 = 150;
palavra_1 = palavra_1 + numero_1;
console.log(palavra_1);
}
/*
const - são variaveis constantes, que não tem o seu valor alterado


const coisa = "teste aleatorio";
coisa = 122; // Isso dá um erro, pq ela não pode ser alterada

*/

/* Trabalhos separados 

Usase as {} para fazer blocos de trabalhos separados
*/
let teste_1;
console.log(teste_1);
{
    teste_1 = 150;
    console.log(teste_1);
}
teste_1 += 150;
console.log(teste_1);

// quando declarar um let dentro de um bloco ele fora do bloco não existe

{
    let teste_2 = "Dentro do bloco";
    console.log(teste_2);
}

// console.log(teste_2) isso dara um erro pq o teste_2 não existe

/*
Funções Function
*/

function PC() {
    let nome = "Guimcv_Pc";
    let processador = "Ryzen 7 5700u";
    let video = "RX6600";
    console.log("o nome do pc é "+nome+"\nO Processador é o: "+processador+"\nE o video é o: "+video);
    // Usa-se a crase para criar um fstring
    console.log(`O nome de pc é ${nome}\nO processador é o: ${processador}\nE a placa de video é a ${video}`); 
};

PC();

/*
Tipo de variavel
*/
{
let int = 120;
let string = "texto";
console.log(typeof int);    // return int
console.log(typeof string); // retunr string

// instanceof

console.log(int instanceof Number) // --> True
console.log(int instanceof Array) // --> False
console.log(string instanceof Array) // --> False


/*Boleano | True or False*/

{
    let number = true;
    let string = false;
    console.log(typeof number);
    console.log(typeof string);
    console.log(number);
    console.log(string);
};

/* Bigint são numeros que quando divisiveis dão o numero inteiro arredondado para baixo */

{
    let number = 50n
    let number_2 = 20n
    console.log(number/number_2)
}

/*
Incerção de aspas duplas ou simples em strings por meio das baras 
*/
{
let message1 = 'The vessel \'Mars\' called at the port.';
let message2 = "Cyclone \"Cilida\" to pass close to Mauritius.";
   
console.log(message1); // -> The vessel 'Mars' called at the port.
console.log(message2); // -> Cyclone "Cilida" to pass close to Mauritius.
   
let path = "C:\\Windows";
console.log(path); // -> C:\Windows
}
/*
Funções do console
*/

console.time() // Inicio do cronometro
console.log("teste ") // Execução dentro do cronometro

console.timeEnd() // fim do cronometro
console.warn("Teste de alerta") // Alerta
console.error("Exibe um erro")

/*
pegar caracteres

variavel.charAT(numero)
variavel.slice(0,5)
variavel.split('') - Separa as palavras de acordo com a regra
*/
{
    let nome = "Guilherme Martins";
    let letra = nome.charAt(2);
    let letra_2 = nome.charAt(0);
    let palavra = nome.slice(0,6);
    let palavra_2 = nome.split(" ");
    console.log(letra); // -> i
    console.log(letra_2); // -> G
    console.log(palavra); // -> Guilhe
    console.log(palavra_2); // -> Guilhe
}
/*
Transformar de novo uma variavel
*/
{
    var nome = "123";
    nome = Number(nome);
    console.log(typeof nome);
}




//SECTION - objetos
{
let objeto = {}; // --> Ele é um objeto
objeto = {
palavra:"Palavra de teste",
numero:150
};

console.log(objeto.palavra) /// --> Palavra de teste
console.log(objeto.numero) /// --> 150


// exemplo de uso

let user1 = {
    name: "Calvin",
    surname: "Hart",
    age: 66,
    email: "CalvinMHart@teleworm.us"
};
   
let user2 = {
    name: "Mateus",
    surname: "Pinto",
    age: 21,
    email: "MateusPinto@dayrep.com"
};

// Pode-se definir a variavel do objeto depois

user1.telefone = "61 98765-4321";
console.log(user1.telefone)
u1t = user1.telefone
console.log(u1t)


//!SECTION - listas

let dias = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta"];
console.log(dias[0]) // --> Domingo

dias[0] = "Sabado"

console.log(dias[0]) // --> Sabado

// lista dentro de lista

let names = [["Olivia", "Emma", "Mia", "Sofia"], ["William", "James", "Daniel"]];
console.log(names[0]); // -> ["Olivia", "Emma", "Mia", "Sofia"]
console.log(names[0][1]); // -> Emma
console.log(names[1][1]); // -> James
   
let femaleNames = names[0];
console.log(femaleNames[0]); // -> Olivia
console.log(femaleNames[2]); // -> Mia

// Objetos dentro de listas

let users =[
    {
    name: "Calvin",
    surname: "Hart",
    age: 66,
    email: "CalvinMHart@teleworm.us"
    },
    {
    name: "Mateus",
    surname: "Pinto",
    age: 21,
    email: "MateusPinto@dayrep.com"
    }
];
   
console.log(users[0].name); // -> Calvin
console.log(users[1].age); // -> 21
}

//SECTION - index

/*
Função indexof

ela retorna o index do inten de acordo com o valor recebido

*/
{
let names = ["Olivia", "Emma", "Mateo", "Samuel"];
console.log(names.indexOf("Mateo")); // -> 2
console.log(names.indexOf("Victor")); // -> -1

// push - insere um objeto no final lista

console.log(names.length); // -> 4
   
names.push("Amelia");
console.log(names.length); // -> 5
console.log(names); // - > ["Olivia", "Emma", "Mateo", "Samuel", "Amelia"]

// Unshift - adiciona um item no inicio da lista

console.log(names.indexOf("Mateo")); // -> 2
console.log(names.indexOf("Victor")); // -> -1

// pop - remove o ultimo item da lista

console.log(names.length); // -> 4
   
let name = names.pop();
console.log(names.length); // -> 3
console.log(name); // -> Samuel
console.log(names); // -> ["Olivia", "Emma", "Mateo"]

// Shift - remove o primeiro item da lista


console.log(names.length);  //  ->  4
   
let  teste =  names.shift();
console.log(teste.length);  //  ->  3
console.log(teste);  //  ->  Olivia
console.log(teste);  //  ->  ["Emma",  "Mateo",  "Samuel"]


// Reverse - ele inverte a ordem da lista

names.reverse();
console.log(names); // -> ["Samuel", "Mateo", "Emma", "Olivia"]

// Slice - Pegar os itens de acordo com o seu index, pegando apenas os numeros após esses index 

{
let names = ["Olivia", "Emma", "Mateo", "Samuel"];
   
let n1 = names.slice(2);
console.log(n1); // -> ["Mateo", "Samuel"]
   
let n2 = names.slice(1,3);
console.log(n2); // -> ["Emma", "Mateo"]
   
let n3 = names.slice(0, -1);
console.log(n3); // -> ["Olivia", "Emma", "Mateo"]
   
let n4 = names.slice(-1);
console.log(n4); // -> ["Samuel"]
   
console.log(names); // -> ["Olivia", "Emma", "Mateo", "Samuel"]
}

}

// concat - pega os intens dentro do objeto para comparar com os que tem no parametro para pegar apenas os que estão fora do parametro
{
let  names  =  ["Olivia",  "Emma",  "Mateo",  "Samuel"];
let  otherNames  =  ["William",  "Jane"];
let  allNames  =  names.concat(  otherNames);
   
console.log(names);  //  ->  ["Olivia",  "Emma",  "Mateo", "Samuel"]
console.log(otherNames);  //  ->  ["William",  "Jane"]
console.log(allNames);  //  ->  ["Olivia",  "Emma",  "Mateo","Samuel", "William",  "Jane"]

}
}

//!SECTION - Funções

//delete

{
    var user = {
        nome:"guilherme",
        idade:17

    }
    delete user.nome
        console.log(user.nome) // indefinido/inesistencia
}

//LINK - inputs do html
{/*

<input id="myId" type="text"></input>
<button onClick="console.log(document.getElementById('myId').value)">Get Text</button>

*/

// Alerta no html

alert("Teste de alerta")
window.alert("Teste 2 de alerta") // ele mostara um outro alerta após o outro alerta ser fechado

// caixa de confirmação do alerta

let decision = window.confirm("Is it OK?"); // abrirar uma caixa de confirmação
console.log(decision); // ele retornara True or False

// exemplo pratico

let remove = confirm("Remove all data?");
let message = remove ? "Deleting Data" : "Cancelled"
console.log(message);

// prompt no alerta

let name = window.prompt("What is your name?", "Seu nome");
name = name ? name : "anonymous"; // define o nome como anonymous se a caixa de entrada não for preenchida
 
let age = prompt("Hello " + name + " how old are you?");
alert(name + " is " + age + " years old");


}