let veiculos = [];

while(true){
    op = prompt(`Sistema de gerenciamento de veiculos\n
        1 | Adicionar veiculos
        2 | Remover veiculos
        3 | Listar veiculos`);
    
    if (op === "0" || op === null) break; // Encerra o programa

    switch(Number(op)){
        case 1: 
            cliente = prompt("Qual o nome do cliente:");
            placa = prompt("Qual a placa do veiculo:");
            cor = prompt("Qual a cor do veiculo");
            entrada = prompt("Qual é o horario de entrada")
            vip = confirm("É vip:")
            veiculo = {
                placa: placa,
                cor: cor,
                entrada: entrada,
                cliente: cliente,
                vip: vip
            };
            veiculos.push(veiculo);
            break;
        case 2:
            if (veiculos.length === 0) {
                alert("Nenhum veiculo cadastrado");
                break;}
            hora = prompt("Que horas são:")
            plac = prompt("Qual a placa do veiculo:")
            let num = 0
            for (i of veiculos){
                num =+ num;
                if (i.placa = plac){
                    if(hora >= i.entarda + 3){
                    
                    console.log("Diaria")
                    break;
                }else if(hora >= i.entarda + 2){
                    console.log("3")

                }else if(hora >= i.entarda + 1){
                    console.log("2")

                }else if(hora >= i.entarda ){
                    console.log("1")
                }else{
                    console.log("erro")
                }
        }}
            alert(veiculos[0].placa == plac)


    }
   
}

