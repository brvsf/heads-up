from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import langchain_core

from src.package.registry import OPENAI_API_KEY


class LLMIntegration:

    @classmethod
    def model(cls, model : str = "gpt-3.5-turbo"):
        """
        Creates and returns an instance of the LLM (Language Model) using the specified model.

        Args:
            model (str): The name of the language model to use. Default is "gpt-3.5-turbo".

        Returns:
            ChatOpenAI: An instance of the LLM with the specified configuration.
        """
        llm = ChatOpenAI(
            model=model,
            max_tokens=50,
            api_key=OPENAI_API_KEY
        )
        return llm

    @classmethod
    def get_prompt(cls, categories : list, template : str) -> langchain_core.prompts.prompt.PromptTemplate:
        """
        Creates and returns a prompt template based on the specified categories and template string.

        Args:
            categories (list): A list of categories to use in the prompt.
            template (str): A string template to create the prompt.

        Returns:
            PromptTemplate: A PromptTemplate object created using the provided categories and template.
        """
        return PromptTemplate(categories=categories, template=template)

    @classmethod
    def setup_conversation_chain(cls, model, prompt : str):
        """
        Sets up a conversation chain using the provided language model and prompt.

        Args:
            model: The language model to use in the conversation chain.
            prompt (str): The prompt to initialize the conversation.

        Returns:
            ConversationChain: A ConversationChain instance with the provided model and memory.
        """
        memory = ConversationBufferMemory(return_messages=True)
        memory.chat_memory.add_user_message(prompt)
        conversation_chain = ConversationChain(llm=model, memory=memory)
        return conversation_chain

    @classmethod
    def update_prompt(cls, conversation_chain, new_prompt: str):
        """
        Updates the conversation chain's prompt by clearing the existing memory and adding a new prompt.

        Args:
            conversation_chain: The conversation chain whose memory will be updated.
            new_prompt (str): The new prompt to set for the conversation chain.
        """
        memory = conversation_chain.memory
        memory.chat_memory.messages = []
        memory.chat_memory.add_user_message(new_prompt)
