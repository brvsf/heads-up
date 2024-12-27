import os

# Enviroment variables
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']

# Famous people
EASY = ["Michael Jackson", "Madonna", "Beyoncé", "Pelé", "Lionel Messi",
    "Cristiano Ronaldo", "Barack Obama", "Albert Einstein", "Oprah Winfrey",
    "Elvis Presley", "Rihanna", "Tom Hanks", "Brad Pitt", "Angelina Jolie",
    "LeBron James", "Taylor Swift", "Will Smith", "Leonardo DiCaprio", "Beyoncé",
    "Justin Bieber", "Kim Kardashian", "Kylie Jenner", "Bill Gates", "Steve Jobs",
    "Queen Elizabeth II", "Winston Churchill", "Frank Sinatra", "Serena Williams",
    "Lady Gaga", "Johnny Depp", "Arnold Schwarzenegger", "Dwayne 'The Rock' Johnson",
    "George Clooney"
]

MEDIUM = [
    "Marilyn Monroe", "Audrey Hepburn", "James Dean", "John Lennon", "Jimi Hendrix",
    "Charles Darwin", "Salvador Dalí", "Albert Einstein", "Picasso", "Nelson Mandela",
    "Helen Keller", "Bob Marley", "David Bowie", "Gandhi", "Nikola Tesla",
    "Al Pacino", "Michael Caine", "Audrey Hepburn", "Frida Kahlo", "Steve Irwin",
    "Ernest Hemingway", "James Stewart", "Kate Middleton", "Humphrey Bogart",
    "Andy Warhol", "John F. Kennedy", "Martin Luther King Jr.", "Eleanor Roosevelt",
    "Marilyn Monroe", "Humphrey Bogart", "Gene Kelly", "Winston Churchill", "Shirley Temple"
]

HARD_BR = [
    "Tarcísio Meira", "Clarice Lispector", "Oscar Niemeyer", "Sérgio Mendes",
    "Elis Regina", "Joaquim Nabuco", "Heitor Villa-Lobos", "Juscelino Kubitschek",
    "Zilda Arns", "Itamar Franco", "Luiz Inácio Lula da Silva", "Ana Costa",
    "Luiza Trajano", "Ana Carolina", "Milton Nascimento", "Sérgio Chapelin",
    "Ruy Barbosa", "Cesária Évora", "Paulo Coelho", "Nélson Rodrigues", "Cartola",
    "Chico Buarque", "Dom Hélder Câmara", "Zico", "Lázaro Ramos", "Glória Pires",
    "Reinaldo Azevedo", "Nélson Piquet", "Caetano Veloso", "Gilberto Gil",
    "Roberto Carlos", "Gabriel Garcia Márquez", "Maria Bethânia"
]

HARD_INT = [
    "Jean-Paul Sartre", "Simone de Beauvoir", "Zadie Smith", "David Attenborough",
    "Václav Havel", "Richard Feynman", "Aung San Suu Kyi", "Gustav Klimt",
    "Isabel Allende", "Rainer Maria Rilke", "Edith Nesbit", "Gabriel García Márquez",
    "Kazuo Ishiguro", "George Orwell", "Nadine Gordimer", "Yoko Ono",
    "Maya Angelou", "Toni Morrison", "Anne Frank", "Salvador Dalí", "Marlene Dietrich",
    "Tenzin Gyatso (Dalai Lama)", "Ruth Bader Ginsburg", "David Lynch",
    "Gina Lollobrigida", "Ludwig van Beethoven", "Gertrude Stein", "Haruki Murakami",
    "Kurt Vonnegut", "J.R.R. Tolkien", "Claude Monet", "Agatha Christie", "Annie Leibovitz"
]

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
A pessoa em questão deve estar dentro das seguintes categorias: {categories}
O nível de dificuldade deve ser: {difficulty}
O jogador fará perguntas de sim ou não para tentar adivinhar.

Responda apenas com:

'Sim'
'Não'
'Pergunta inválida' (se a pergunta não puder ser respondida com "Sim" ou "Não").
O jogo termina quando o jogador adivinhar corretamente ou desistir.
"""

TEMPLATE_EN = """ You are participating in a game called 'Heads Up'.
Your role is to help the player guess the person you are thinking of.
The person in question must belong to the following categories: {categories}.
The difficulty level should be: {difficulty}. The player will ask yes or no questions to try to guess.

Respond only with:

'Yes'
'No'
'Invalid question' (if the question cannot be answered with "Yes" or "No").
The game ends when the player guesses correctly or gives up.
"""

# Mapping dicts
difficulty_mapping = {
    'Easy': EASY,
    'Fácil': EASY,
    'Medium': MEDIUM,
    'Médio': MEDIUM,
    'Hard': HARD_INT,
    'Difícil': HARD_BR,
}

template_mapping = {
    'Português' : TEMPLATE_PT,
    'English' : TEMPLATE_EN
}
