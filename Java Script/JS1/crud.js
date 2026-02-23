// A lista deve ficar FORA do loop para não ser apagada
const produtos = []; 

while (true) {
    let op = prompt("Selecione uma opção:\n1 | Criar produto\n2 | Listar produtos\n3 | Atualizar produtos\n4 | Deletar produtos\n0 | Sair");
    
    if (op === "0" || op === null) break; // Encerra o programa

    switch (Number(op)) {
        case 1:
            let nome = prompt("Qual o nome do produto:");
            let quant = parseInt(prompt("Qual a quantidade do produto:"));
            let valor = parseFloat(prompt("Qual o valor do produto:"));
            
            // Adicionando o objeto à array global
            produtos.push({
                nome: nome,
                quantidade: quant,
                valor: valor
            });
            alert("Produto cadastrado com sucesso!");
            break;

        case 2:
            if (produtos.length === 0) {
                alert("Nenhum produto cadastrado.");
            } else {
                let listagem = "--- Lista de Produtos ---\n";
                produtos.forEach((p, index) => {
                    listagem += `${index} | Nome: ${p.nome} | Qtd: ${p.quantidade} | Preço: R$ ${p.valor.toFixed(2)}\n`;
                });
                console.log(listagem);
                alert(listagem); // Exibe no navegador para facilitar
            }
            break;

        default:
            alert("Opção inválida!");
            break;
    }
}
