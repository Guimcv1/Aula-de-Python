var lista = [];
var fechar = false;
while (!fechar){
    var nome = prompt("Coloque um nome ou cancele para fechar");

    if (nome != null){
        lista.push(nome);
    }else{
        fechar = true;
    }
}
for(var i = 0; i < lista.length; i++){
    console.log(lista[i]);
};