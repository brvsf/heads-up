from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import langchain_core

from src.package.registry import OPENAI_API_KEY


class LLMIntegration:

    @classmethod
    def model(cls, model : str = "gpt-3.5-turbo"):
        """"""
        llm = ChatOpenAI(
            model=model,
            max_tokens=50,
            api_key=OPENAI_API_KEY
        )
        return llm

    @classmethod
    def get_prompt(cls, categories : list, template : str) -> langchain_core.prompts.prompt.PromptTemplate:
        return PromptTemplate(categories=categories, template=template)

    @classmethod
    def setup_conversation_chain(cls, model, prompt : str):
        memory = ConversationBufferMemory(return_messages=True)
        memory.chat_memory.add_user_message(prompt)
        conversation_chain = ConversationChain(llm=model, memory=memory)
        return conversation_chain
