"""This file will host the main code related to Pet Names Generator."""
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from llm.openai import get_openai_llm


def generate_pet_name(animal_type: str, color: str):
    """This function will generate Pet Names using LLM."""
    llm = get_openai_llm(temperature=0.7)

    prompt = PromptTemplate(
        input_variables=['animal_type', 'color'],
        template="I have a pet {animal_type} and it is {color} in color. I want a cool name for "
                 "it. Suggest to me five cool names for my pet. Give me just the names and "
                 "nothing else."
    )

    chain = LLMChain(
        llm=llm,
        prompt=prompt
    )
    
    return chain({'animal_type': animal_type, "color": color})


if __name__ == "__main__":
    print(generate_pet_name(animal_type="dog", color="black"))
