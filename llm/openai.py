"""This file contains the code for the OpenAI model."""
import os

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_openai_llm(temperature: float = 0.0):
    """This function returns the OpenAI LLM object."""
    return OpenAI(
        model=os.getenv("MODEL"),
        temperature=temperature,
        max_retries=2,
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )
