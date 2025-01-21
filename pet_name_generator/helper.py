"""This file will host the main code related to Pet Names Generator."""
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType

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


def get_langchain_agent():
    llm = get_openai_llm(temperature=0.5)

    tools = load_tools(["wikipedia", 'llm-math'], llm=llm)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    print(
        agent.run(
            "What is the average age of a cat? What is the sum of the expected age of 3 cats?"
        )
    )


if __name__ == "__main__":
    # print(generate_pet_name(animal_type="dog", color="black"))
    get_langchain_agent()
