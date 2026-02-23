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