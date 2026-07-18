🍳 Agente de IA — Cozinheira Profissional

Um agente de inteligência artificial desenvolvido em Python utilizando a biblioteca Agno e o modelo GPT-4o Mini da OpenAI. O projeto permite interagir com uma assistente especializada em culinária diretamente pelo terminal.

✨ Funcionalidades
Assistente especializada em culinária
Responde perguntas sobre receitas e ingredientes
Fornece dicas de preparo e técnicas de cozinha
Interface simples via terminal
Encerramento com o comando sair
🛠️ Tecnologias
Python 3.10+
Agno
OpenAI API
python-dotenv
📁 Estrutura do Projeto
.
├── main.py
├── .env
├── requirements.txt
└── README.md
🚀 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

Acesse a pasta do projeto:

cd seu-repositorio

Instale as dependências:

pip install agno openai python-dotenv
⚙️ Configuração

Crie um arquivo .env na raiz do projeto e adicione sua chave da OpenAI:

OPENAI_API_KEY=sua_chave_da_openai
▶️ Como executar

Execute o projeto:

python main.py
💬 Exemplo
Digite: Como faço um bolo de chocolate?

Resposta:
Para preparar um bolo de chocolate macio você vai precisar de...

Para encerrar:

Digite: sair

Encerrando Agent 🤖
🧠 Configuração do Agente
Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é uma cozinheira profissional",
    markdown=True
)

A descrição define o comportamento do agente, fazendo com que todas as respostas sejam voltadas para culinária.

💡 Exemplos de perguntas
Como fazer arroz soltinho?
Qual o melhor tempero para carne?
Como substituir ovos em uma receita?
O que posso fazer com frango e batata?
Como armazenar alimentos corretamente?
📄 Licença

Este projeto é destinado a fins de estudo e aprendizado.

<div align="center">

Desenvolvido com Python, Agno e OpenAI.

</div>