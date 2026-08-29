from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
# text-embedding-ada-002,text-embedding-3-large,text-embedding-3-small
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", diimensions=64)

texts = [
    "Hello myself Laxmi Jindal",
    "Welcome to my github laxmijin11-cyber",
    "you all are cute people",
]

vector = embeddings.embed_documents(texts)
# vector = embeddings.embed_query("You are going to learn")
print(vector)
