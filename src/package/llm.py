from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import langchain_core

from src.package.registry import OPENAI_API_KEY


class LlmIntegration:

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
    def get_response(
        cls,
        prompt : langchain_core.prompts.prompt.PromptTemplate,
        categories : list,
        difficulty : str) -> str:
        categories_str = ", ".join(categories)
        return prompt.format(categories=categories_str, difficulty=difficulty)
