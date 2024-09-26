from omniprompt.code_tasks import code_refiner_prompt
from omniprompt.data_analysis import pandas_prompt
from langchain_groq import ChatGroq
import os

GROQ_API_KEY = "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"

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = ChatGroq(temperature = 0.4, model_name="llama3-8b-8192")

user_query = "I want to see how many duplicate values i have in my df and then remove them"

prompt = pandas_prompt(user_query)
response = llm.invoke(prompt)

print(response.content)

prompt = code_refiner_prompt(response, "python")
response = llm.invoke(prompt)

print(response.content)