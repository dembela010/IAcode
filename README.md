🍳 Agente de IA - Cozinheira Profissional

Um projeto simples em Python que utiliza a biblioteca Agno e o modelo GPT-4o Mini da OpenAI para criar uma assistente virtual especializada em culinária. O agente responde perguntas sobre receitas, técnicas de cozinha, ingredientes e dicas gastronômicas diretamente pelo terminal.

📋 Funcionalidades
🤖 Agente de IA especializado em culinária.
🍝 Responde dúvidas sobre receitas e ingredientes.
🔥 Dá dicas de preparo e técnicas de cozinha.
💬 Interface simples via terminal.
✅ Encerramento do programa com o comando sair.
🛠️ Tecnologias utilizadas
Python 3.10+
Agno
OpenAI API
python-dotenv
📦 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

Entre na pasta:

cd seu-repositorio

Instale as dependências:

pip install agno openai python-dotenv
⚙️ Configuração

Crie um arquivo chamado .env na raiz do projeto.

Exemplo:

OPENAI_API_KEY=sua_chave_da_openai
▶️ Executando o projeto

Execute:

python main.py

Exemplo de uso:

Digite: Como faço um bolo de chocolate?

Resposta:
Para fazer um bolo de chocolate você precisará de...

Para encerrar:

Digite: sair
Encerrando Agent 🤖
📂 Estrutura do projeto
.
├── main.py
├── .env
├── README.md
└── requirements.txt
📄 Código principal

O projeto cria um agente utilizando o modelo GPT-4o Mini com a seguinte descrição:

description="Você é uma cozinheira profissional"

Isso faz com que todas as respostas sejam voltadas para culinária.

📌 Exemplo de perguntas
Como fazer pão caseiro?
Qual a diferença entre fermento biológico e químico?
Como cozinhar arroz soltinho?
Qual o melhor tempero para frango?
Como substituir ovos em uma receita?