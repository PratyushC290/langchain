from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions = 300)

documents = ['Deep learning models use multiple layers of artificial neurons to extract hierarchical features from raw data.',
             'Backpropagation and gradient descent are essential techniques for training deep neural networks effectively.',
             'Convolutional Neural Networks (CNNs) excel at image recognition tasks by leveraging spatial hierarchies in data.',
             'Deep learning requires large amounts of labeled data and high computational power for effective training and generalization.',
             'Activation functions like ReLU, Sigmoid, and Tanh introduce non-linearity in deep neural networks, enabling complex decision boundaries.',
             'Transfer learning allows deep learning models to leverage pre-trained knowledge, reducing training time and improving performance on new tasks.']


query = 'explain convolutional neural networks'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

cos = cosine_similarity([query_embedding],doc_embeddings)[0]
#both values in cosine similarity should be 2D vectors
#output is a 2d list so we use [0] to get a 1d list
#[[0.17871483 0.29040145 0.1738624  0.17390606 0.08089984 0.58142645 0.20274595]] is the 2d output without [0]

index, score = sorted(list(enumerate(cos)), key =lambda x:x[1])[-1]
#sorted on the basis of cosine similarity and then take the largest one

print(query)
print(documents[index])
print(f"similarity score = {score}")