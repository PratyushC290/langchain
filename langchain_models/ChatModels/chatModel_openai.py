from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() 

model = ChatOpenAI(model = 'gpt-4')

answer = model.invoke("Who wrote the book titled the tale of two cities?", temperature = 0.6, max_completion_tokens = 10)
# Lower temp->More deterministic, Higher Temp->More creative, range=(0,2)
'''
Temperature = 0 always gives the same value as answer for the same question
Factual answers(math, code, facts)->(0.0,0.3)
balanced response(general questions, explainantion)->(0.5,0.7)
creating writing, storytelling, jokes->(0.9,1.2)
max randomness (wild ideas, brainstorming)->1.5+
'''
# max_completion_token = max no of tokens in output (tokenisation)

print(answer.content)