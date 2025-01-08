## Heads-up chatbot

This repository contains a project demonstrating how to build a fun and interactive chatbot for a game where players guess the famous person the bot is "thinking" of. Inspired by popular games like "Heads-Up" or "Who Am I," players ask yes-or-no questions to narrow down their guesses. The chatbot leverages LangChain, OpenAI's ChatGPT API, and Streamlit for the game interface, along with Slack integration for team play.

## Features

- **LangChain Framework**: Manages the logical flow of questions and answers to simulate a real-time guessing game.
- **OpenAI ChatGPT API**: Provides intelligent and context-aware responses to player questions.
- **Streamlit Frontend**: An intuitive web interface for solo or group gameplay.
- **Slack Integration**: Enables multiplayer game sessions directly within a Slack workspace.
- **Multilingual Support**: Players can select their preferred language (English or Portuguese) for both questions and responses.

---

## Language Selection

The chatbot supports English and Portuguese. You can select the language:
- **Streamlit Interface**: Use the dropdown menu to switch between languages.
- **Slack Bot**: Change the language via a specific command (e.g., `/language`).

All responses and game interactions will adapt to the chosen language for a more inclusive experience.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/brvsf/heads-up.git
   cd heads-up
   ```

2. Create a virtual environment and activate it:
   ```bash
    pyenv virtualenv 3.10.6 heads-up
    pyenv local heads-up
   ```

3. Install the required dependencies:
   ```bash
   make setup
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   SLACK_BOT_TOKEN=your_slack_bot_token
   SLACK_SIGNING_SECRET=your_slack_signing_secret
   ```

## Usage

### Streamlit Game Interface

1. Run the Streamlit app:
   ```bash
   make app
   ```
2. Open the app in your browser at [http://localhost:8501](http://localhost:8501).
3. Begin the guessing game by asking yes-or-no questions to uncover the famous person the bot has in mind.

### Slack Bot

1. Ensure your bot is added to your Slack workspace.
2. Run the Slack integration script:
   ```bash
   python slack_bot.py
   ```
3. Play the game with your team by interacting with the bot in Slack channels or direct messages.

## Project Structure

```
.
├── LICENSE                   # License file for the project.
├── Makefile                  # File containing build and automation commands.
├── README.md                 # Project documentation.
├── requirements.txt          # List of project dependencies.
├── setup.py                  # Setup script for package installation.
├── src                       # Source code for the application.
│   ├── __init__.py           # Initialization file for the src module.
│   ├── AboutUsEN.py          # "About Us" page content in English.
│   ├── AboutUsPT.py          # "About Us" page content in Portuguese.
│   ├── App.py                # Streamlit main application hub.
│   ├── HeadsUp.py            # Streamlit page for the game logic.
│   ├── languages             # Directory for language-specific content.
│   │   ├── __init__.py       # Initialization file for the languages module.
│   │   ├── English.py        # Strings and configurations for the English language.
│   │   ├── Portuguese.py     # Strings and configurations for the Portuguese language.
│   ├── package               # Core components of the chatbot logic.
│   │   ├── __init__.py       # Initialization file for the package module.
│   │   ├── llm.py            # Management of the language model (LLM) interactions.
│   │   ├── registry.py       # Handles data storage and configuration settings.
│   │   ├── utils.py          # Helper and utility functions for the application.
└── tests                     # Directory for test cases.
    ├── __init__.py           # Initialization file for the tests module.
    └── tests.py              # Unit tests for application functionality.

```

## Customization

Feel free to extend the project by:
- Adding more famous personalities or categories.
- Enhancing the question logic or difficulty levels in `chatbot.py`.
- Adding scorekeeping or multiplayer support in `slack_bot.py`.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request if you'd like to suggest improvements or fix bugs.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [LangChain](https://langchain.com) for the framework.
- [OpenAI](https://openai.com) for the ChatGPT API.
- [Streamlit](https://streamlit.io) for the interactive interface.
- [Slack API](https://api.slack.com) for real-time communication.

---

Enjoy playing and guessing with the LangChain-powered game bot! 🚀
