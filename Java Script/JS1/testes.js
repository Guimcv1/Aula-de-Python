// CRUD
/*

Create
read
update
delete

*/
{
while(true){
    var produtos =[]
    var op = prompt("Selecione uma opção:\n1 | Criar produto\n2 | Listar produtos\n3 | Atualizar produtos\n4 | Deletar produtos")
    op = Number(op)
    switch (op){
        case 1:
            let prod_nome = prompt("Qual o nome do produto:")
            let prod_quant = prompt("Qual a quantidade do produto:")
            let prod_valor = prompt("Qual o valor do produto:")
            let produto = {
            produto_nome: prod_nome,
            produto_quantidade: prod_quant,
            produto_valor: prod_valor,
            }
            produtos.push(produto)
            continue;
        case 2:
            for(let i of produtos){
                console.log(`\n${50*"-"}\nProduto: ${i.produto_nome}\nQuantidade: ${i.produto_quantidade}\nValor: ${i.produto_valor}`)}
            
        case _:
            break;
            

}}



}