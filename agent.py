#Importando os frameworks necessários para o projeto
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

#Ler o .env
load_dotenv()

agente = Agent(
 model=OpenAIChat(id="gpt-4o-mini"),
 description="Voce é uma cozinheira profissional",
 markdown=True
)


while True:

    pergunta = input("Digite: ")
    if pergunta == "sair":
        print("Encerrando Agent 🤖")
        break
    else:
        agente.print_response(pergunta)