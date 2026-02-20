/*
Variaveis 

let - Não funciona fora dos blocos
var - Funciona fora dos blocos

*/

let numero = 150;
console.log(numero);

/*
A maioria das coisas sõa bastante parecidas com python

sistemas de operadores
variaveris
redefinição

*/

let palavra_1 = "Esta é uma palavra ";
let numero_1 = 150;
palavra_1 = palavra_1 + numero_1;
console.log(palavra_1);

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
};

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

let message1 = 'The vessel \'Mars\' called at the port.';
let message2 = "Cyclone \"Cilida\" to pass close to Mauritius.";
   
console.log(message1); // -> The vessel 'Mars' called at the port.
console.log(message2); // -> Cyclone "Cilida" to pass close to Mauritius.
   
let path = "C:\\Windows";
console.log(path); // -> C:\Windows

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
    console.log(typeof nome)
}
