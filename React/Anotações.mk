#ANCHOR - O que é o react

* O react é uyma biblioteca usada para criar interfaces de usuário interativas
* Componentes
	* react utiliza de varios componentes juntos para criar uma aplicação interativa e uma grande estrutura
* Desenvolvido pelo o facebook 
* Aprende apenas uma vez e pode usar em qualquer lugar
	*IOS & Android (react Native) & Desktop (Electron)
* Formato de arquivo jsx

#ANCHOR - Necessario instalar o NODEJS e NPM

*NODEJS é um interpretador
*NPM é uma buscador de bibliotecas e arrumador de problemas

*Necessario instalar o Tailwind CSS, prettier e o ESLint
*Ir nas configurações e ativar o:
	*format on save
	*default formatter e selecionar o prettier

#ANCHOR Configurar o nodejs

*Digite node -v

*Ele retornara a versão do nodejs

#ANCHOR - Vite 

* Instalar o vite Digite
npm create vite@5.2.2 .
*selecione o react depois o javascript
npm install

*Para rodar a aplicação use:
npm run dev

#ANCHOR - Pagina HTML

*SPA (Single Page Application)

* Ultilizase o html sem conteudo é apenas um bote espiatorio
* O conteudo é inserido pelo o Javascript (React)

*Vantagens de SPA:
	*Velocidade: navegação entre páginas é muito mais rápio, pois não exige chamadas para um servidor
	*Experiencia de Usuario: SPA são altamente interativas e performáticas

#ANCHOR - jsx

Cada função do JS é um componente e só pode retornar 1 elemento, não mais que 1, ex: 
funtion App(){
	return(
		<div>
			<h1>Olá mundo</h1>
		</div>
	);
}

export default App;

*FIXME - Não pode ser 2 ou mais assim darar um erro

funtion App(){
	return(
		<div>
			<h1>Olá mundo</h1>
		</div>

		<div>
			<h1>Odeio o mundo</h1>
		</div>
	);
}

export default App;

*NOTE - States (Estado)

o state commita e da um reupload da pagina

import { useState } from "react";
 
const [] = useState()

*O use state é uma função do react que permite a ultilização de outras funções do react 
ele é como se fosse uma biblioteca que importa varias funções como o State

o useState faz com que ao iniciar uma operação ele renderiza a pagina de novo, com um novo valor agregado

*REVIEW - Botões

import { useState } from "react";

function App(){


  const titulo = 'React'  //const é uma função não modificavel
  let mensagem = '------------'    //let é uma função modificavel

  const [mensage, setMassage] = useState("Olá Mundo!") // Ele é o equivalente ao o .replaced(useState, setMassage)
  const [bits, setReact] = useState("Native!") // Ele é o equivalente ao o .replaced(useState, setMassage)

  return (
    <div>
        <h1>{titulo}</h1>
        <h1>{bits}</h1>
        <h1>{mensagem}</h1>
        <h1>{mensage}</h1>
        <button onClick={() => {
          setMassage("Olá Inferno!")
        }}>Mudar Mundo</button>
        <button onClick={() => {
          setMassage("Olá Mundo!")
        }}>Mudar Inferno</button>
        <button onClick={()=>{setMassage("Eita")}}>Bo
          
          
          tão</button >
        <button onClick={()=>{setReact("Bits!")}}>Native/Bits</button>
        <button onClick={()=>{setReact("Native!")}}>Bits/Native</button>
    </div>
  );
}

export default App;

*REVIEW - 

*ANCHOR - Instalar o Tailwind - https://v3.tailwindcss.com/docs/guides/vite

npm install -D tailwindcss@3.4.10 postcss@8.4.41 autoprefixer@10.4.20
npx tailwindcss init -p

# Arquivo tailwind.config.js -----------------------

content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],

# Index.CSS ----------------------------------------

@tailwind base;
@tailwind components;
@tailwind utilities;

#-------- Reinicie o programa ----------------------


Tailwind

É um estilizador te css usando classes proprietarias como um "Vertical-Animation()"


# Lucide react

npm install lucide-react@0.435.0

import { ChevronRightIcon } from "lucide-react";

lucide é uma feramenta para colocar diversos pack de icones modificaveis como setas e quedrados e outras coisas

#--------------------------------------------------

const [tasks, setTasks] = useState()

esta é uma função que é ultilizada para atualizar a pagina após uma interação com um novo valor atribuido
é uma constante/função que que coloca a variavel, valor final, valor inicial

ex: ao clicar em um botão chamado banana ele vira maça

const [fruta, setFruta] = useState("banana")

<h1>{fruta}</h1>

<button onClick={() => setFruta('maça')}>Tranformar banana em maça</button>


#--------------------------------------------------

function 