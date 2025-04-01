from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

wordVec = embedding.embed_query("Hi my name is Pratyush!")

print(str(wordVec))

'''just the same thing for embed_documents as done in openai_docs.py 
i.e. create a list doc and then pass it to embedding.embed_documents(doc)'''