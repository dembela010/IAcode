<div align="center">

# 🍳 Agente de IA — Cozinheira Profissional

Um agente de inteligência artificial desenvolvido em **Python** utilizando **Agno** e **OpenAI** para responder perguntas sobre culinária diretamente pelo terminal.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--Mini-412991?style=for-the-badge)
![Agno](https://img.shields.io/badge/Framework-Agno-black?style=for-the-badge)

</div>

---

## 📖 Sobre

Este projeto cria um agente conversacional especializado em culinária utilizando a biblioteca **Agno**. O usuário pode fazer perguntas sobre receitas, ingredientes, técnicas de preparo e receber respostas geradas pelo modelo **GPT-4o Mini** da OpenAI.

---

## ✨ Funcionalidades

- 🍝 Responde dúvidas sobre receitas
- 🥘 Sugere pratos e ingredientes
- 🔥 Explica técnicas culinárias
- 💬 Interface simples via terminal
- ⚡ Respostas em Markdown
- 🚪 Encerramento com o comando `sair`

---

## 🛠️ Tecnologias

| Tecnologia | Descrição |
|------------|-----------|
| Python | Linguagem principal |
| Agno | Framework para criação do agente |
| OpenAI | Modelo de linguagem |
| python-dotenv | Gerenciamento das variáveis de ambiente |

---

## 📂 Estrutura

```text
.
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Entre na pasta

```bash
cd seu-repositorio
```

### 3. Instale as dependências

```bash
pip install agno openai python-dotenv
```

---

## 🔑 Configuração

Crie um arquivo `.env` na raiz do projeto.

```env
OPENAI_API_KEY=sua_chave_da_openai
```

---

## ▶️ Executando

```bash
python main.py
```

---

## 💻 Exemplo de uso

```text
Digite: Como faço um molho branco?

Resposta:

Para preparar um molho branco clássico você vai precisar de:

• Manteiga
• Farinha de trigo
• Leite
• Sal
• Noz-moscada

...
```

Para finalizar:

```text
Digite: sair

Encerrando Agent 🤖
```

---

## 🧠 Configuração do Agente

```python
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é uma cozinheira profissional",
    markdown=True
)
```

---

## 💬 Exemplos de perguntas

- Como fazer arroz soltinho?
- Qual o melhor corte para churrasco?
- Como substituir ovos em uma receita?
- Quanto tempo cozinhar macarrão?
- O que fazer com peito de frango?

---

## 📌 Próximas melhorias

- [ ] Interface Web
- [ ] Histórico de conversas
- [ ] Memória entre sessões
- [ ] Escolha de diferentes especialidades
- [ ] Suporte a múltiplos modelos

---

## 📄 Licença

Este projeto é destinado para fins de estudo e aprendizado.

---

<div align="center">

Desenvolvido com ❤️ utilizando **Python**, **Agno** e **OpenAI**.

</div>