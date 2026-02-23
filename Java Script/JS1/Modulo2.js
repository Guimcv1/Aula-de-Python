// Funções dentro de objetos
{
    let objeto = {
        nome:'guilherme',
        telefone:"61 98765-4321",
        idade:18,
        funcao: function funcao(entrada){return entrada+objeto.idade}
    }
    let retorno = objeto.funcao(16);
    console.log(retorno)
}

// Objetos dentro de objetos
{
let objeto = {
    nome:"nunes",
    idade:19,
    objeto2:{
        sobrenome:"carvalho",
        objeto3:{
            numero:"61 98765-4321"
        }
    }
}

console.log(objeto.objeto2.objeto3.numero)
}

// deletar objetos

{
    let lista = [
    {
        nome:"guilherme",
        idade:18
    },
    {
        nome:"guilherme",
        idade:18
    }
    ];
    delete lista[0].nome;
    console.log(lista[0].nome)
}

// forEach - ele tem as mesmas funções que o for in

{
    let lista = [
        {nome:"teste",
         idade:50
        },
        {nome:"teste_2",
         idade:510
        }
    ]
    listagem = "---- Listagem de pessoas -----"
    lista.forEach((i, index) => {
        listagem += `${index} | Nome: ${i.nome} | Idade: ${i.idade}\n`;
    })
    console.log(listagem)

}

// Funções de linha
{
() => {} // Estrutura basica
let c = (entrada) =>  a = entrada + 150 
let b = (entrada) => {return a = entrada + 150 } // Usa-se o return e os colcheites quando vai se adicionar mais propriedades no objeto
console.log(b(5))

}

// Map

const usuarios = [
    { nome: "Ana", idade: 25 },
    { nome: "Bruno", idade: 30 },
    { nome: "Carla", idade: 28 }
];

// Extrair apenas os nomes
const nomes = usuarios.map(usuario => usuario.nome);

console.log(nomes); // ["Ana", "Bruno", "Carla"]


