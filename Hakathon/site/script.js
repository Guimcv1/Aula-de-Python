// script.js

// Seleções dos elementos
const primaryBtn = document.getElementById('primaryBtn');
const outlineBtn = document.getElementById('outlineBtn');
const dangerBtn = document.getElementById('dangerBtn');
const limparBtn = document.getElementById('limparBtn');
const demoForm = document.getElementById('demoForm');
const output = document.getElementById('output');
const openTabBtn = document.getElementById('openTabBtn');

// Função utilitária para logar na área de saída
function log(msg){
  const time = new Date().toLocaleTimeString();
  output.textContent += `[${time}] ${msg}\n`;
  // rolar para o fim
  output.scrollTop = output.scrollHeight;
}

// Eventos dos botões
primaryBtn.addEventListener('click', () => log('Você clicou no botão primário'));
outlineBtn.addEventListener('click', () => log('Você clicou no botão outline'));
dangerBtn.addEventListener('click', () => {
  if (confirm('Tem certeza que quer executar ação de perigo?')) log('Ação de perigo confirmada');
  else log('Ação de perigo cancelada');
});

// Limpar campos
limparBtn.addEventListener('click', () => {
  demoForm.reset();
  log('Formulário limpo');
});

// Envio do formulário — validação simples
demoForm.addEventListener('submit', (e) => {
  e.preventDefault(); // evita envio real
  const nome = demoForm.nome.value.trim();
  const email = demoForm.email.value.trim();
  const mensagem = demoForm.mensagem.value.trim();

  if (!nome || !email) {
    log('Por favor preencha nome e email.');
    return;
  }

  // Simulamos um envio
  log(`Enviando dados — nome: ${nome}, email: ${email}, mensagem: ${mensagem || '(vazia)'} `);
  // Aqui você poderia fazer fetch() para enviar para um servidor
  setTimeout(() => log('Envio simulado concluído.'), 700);
});

// Abrir nova aba via JS — usar com parcimônia (pode ser bloqueado por pop-up blockers se não for ação direta do usuário)
openTabBtn.addEventListener('click', () => {
  const url = 'https://developer.mozilla.org/';
  // window.open retorna a janela aberta (ou null se bloqueada)
  const newWindow = window.open(url, '_blank', 'noopener,noreferrer');
  if (newWindow) {
    log('Nova aba/janela aberta com sucesso.');
  } else {
    log('Falha ao abrir nova aba — possivelmente bloqueada pelo navegador.');
  }
});

// Boas práticas: prevenir comportamento padrão quando aplicável e adicionar atributos acessíveis no HTML
