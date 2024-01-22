import os
import openai
from text_processing import load_pdf
from config import *
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def equation_classifier(text, equation):
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=CLASSIFIER_GPT_MODEL, temperature=CLASSIFIER_TEMPERATURE, max_tokens=MAX_TOKEN_LIMIT)
    prompt = PromptTemplate(
        template=GPT_CLASSIFICATION,
        input_variables=["text", "equation"], )
    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run(text=text, equation=equation)
    return output


def equation_solver(equation):
    pdf_documents_path = os.listdir(DATA_PATH)
    for pdf_path in pdf_documents_path:
        instructions = load_pdf(os.path.join(DATA_PATH, pdf_path))
        classification_result = equation_classifier(instructions, equation)
        print(classification_result)
        if classification_result == "T":
            llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=SOLVER_GPT_MODEL, temperature=SOLVER_TEMPERATURE)
            prompt = PromptTemplate(
                template=GPT_MATH_SOLVE,
                input_variables=["instructions", "equation"], )
            # Initialize chain
            chain = LLMChain(llm=llm, prompt=prompt)
            output = chain.run(instructions=instructions, equation=equation)
            return output
    return f"Sorry but we don`t know how to solve this equation..."