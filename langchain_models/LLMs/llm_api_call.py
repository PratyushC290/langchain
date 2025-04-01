from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

gpt = OpenAI(model='gpt-3.5-turbo-instruct')

ans = gpt.invoke("What is simlipal kai chutney madeup of?")
print(ans)