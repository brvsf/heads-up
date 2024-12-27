import os

# Enviroment variables
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']


OPTIONS_PT = [
    'Atores', 'Musicos', 'Pintores', 'Cientistas', 'Personagens'
]

OPTIONS_EN = [
    'Actors', 'Musicians', 'Painters','Scientists', 'Characters'
]

# Initial prompts
TEMPLATE_PT = """
Você está participando de um jogo chamado 'Heads Up'.
Seu papel é ajudar o jogador a adivinhar a pessoa em que você está pensando.
A pessoa em questão deve estar dentro das seguintes categorias: {categories} como sua principal forma de fama.
O nível de dificuldade deve ser: {difficulty}. A dificultade está relacionada com o quão famosa a pessoa é.
O jogador fará perguntas de sim ou não para tentar adivinhar.

Responda apenas com:

'Sim'
'Não'
'Pergunta deve ser de sim ou não.' (se a pergunta não puder ser respondida com "Sim" ou "Não").
O jogo termina quando o jogador adivinhar corretamente ou desistir.

Caso o jogador acerte voce deve falar 'Parabéns! Você acertou!'.
Caso o jogador desista voce deve falar o nome da pessoa selecionada.
"""

TEMPLATE_EN = """
You are participating in a game called 'Heads Up'.
Your role is to help the player guess the person you are thinking of.
The person in question must belong to the following categories: {categories} as their main form of fame.
The difficulty level should be: {difficulty}. The difficulty relates to how famous the person is.
The player will ask yes or no questions to try to guess.

Respond only with:

'Yes'
'No'
"It should be a 'yes' or 'no' question." (if the question cannot be answered with "Yes" or "No").
The game ends when the player guesses correctly or gives up.

If the player guesses correctly, you should say 'Congratulations! You got it right!'.
If the player gives up, you should say the name of the selected person.
"""

# How to play

HOW_TO_PLAY_PT = """
# Como Jogar Heads-Up

## Objetivo:
O objetivo do jogo é adivinhar o nome de uma pessoa famosa ou personagem que está na cabeça do jogador, fazendo perguntas que podem ser respondidas com "sim" ou "não".

## Regras:
1. **Preparação**: O jogador escolhe uma categoria e uma dificuldade para adivinhar uma pessoa ou personagem famoso.
2. **Jogabilidade**: O jogador deve fazer perguntas ao GuessMaster para descobrir quem é a figura.
3. **Respostas**: GuessMaster responderá apenas com sim ou não.

## Dicas:
- Faça perguntas amplas no início para reduzir as opções rapidamente.
- Use perguntas sobre características físicas, profissões ou períodos históricos.
"""

HOW_TO_PLAY_EN = """
# How to Play Heads-Up

## Objective:
The objective of the game is to guess the name of a famous person or character that is on the player's head by asking questions that can be answered with "yes" or "no".

## Rules:
1. **Preparation**: The player chooses a category and difficulty to guess a famous person or character.
2. **Gameplay**: The player must ask questions to the GuessMaster to figure out who the character is.
3. **Answers**: The GuessMaster will only respond with "yes" or "no".

## Tips:
- Ask broad questions at the beginning to quickly narrow down the options.
- Use questions about physical traits, professions, or historical periods.
"""

template_mapping = {
    'Português' : TEMPLATE_PT,
    'English' : TEMPLATE_EN
}
