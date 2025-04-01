from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv() 

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 128)

king = embedding.embed_query('king')

print(str(king))