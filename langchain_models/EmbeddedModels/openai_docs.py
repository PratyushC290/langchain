from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv() 

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)

documents = [
    "IIT Patna is in Bihta and not actually in Patna",
    "The midsems were unusually tough this time",
    "Everyone is eagerly waiting for the summer holidays"
]

doc = embedding.embed_documents(documents)

print(str(doc))