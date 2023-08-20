import weaviate
import os
import openai

OPENAI_API_KEY=''

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

from tqdm.auto import tqdm
from time import sleep
from uuid import uuid4
import tiktoken
from langchain.text_splitter import TokenTextSplitter


text = response_json


text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=10)
input_chunks = text_splitter.split_text(text)

## Weaviate keys configuration

#Get you API key and URL from Weaviate
auth_config = weaviate.AuthApiKey(api_key="")
client = weaviate.Client(auth_client_secret=auth_config, url="")  # Replace the URL with that of your Weaviate instance

## Weaviate Class details

client.schema.get()  # Get the schema to test connection
# Uncomment the below code when you want to delete your Class on weaviate
# client.schema.delete_class('test')

## Embedding Model and Batch Size

embed_model = "text-embedding-ada-002"

## Creating Embedding

def create_embeddings(texts):
  res = openai.Embedding.create(input=texts, engine=embed_model)
  for record in res['data']:
    embeds = record['embedding']
  return embeds

#Make sure the knowledge name is the name of your class in weaviate
final_chunks=[]
final_chunks.extend([{
   "id": str(uuid4()),
   "text": input_chunks[i],
   "chunk": i,
   "knowledge_name": "knowledge",
   "embeds" : create_embeddings(input_chunks[i]),
} for i in range(len(input_chunks))])

#This cell can be skipped if your class already exists
#class: "Give the name for your class"
class_obj = {
    "class": "test",
    "vectorizer": "text2vec-openai",
}

# Add the class to the schema
client.schema.create_class(class_obj)

vector_ids = []

#Make sure the data_object is the name of your class in weaviate
with client.batch as batch:
  for chunk in final_chunks:
    data_object = {key: value for key, value in chunk.items() if key != "id" and key != 'embeds'}
    vector_ids.append(chunk["id"])
    batch.add_data_object(data_object, "Knowledge", uuid=chunk["id"], vector=chunk["embeds"])

#This cell can be used to check if the embedding has been created as expected
#Make sure the class_name is the name of your class on weaviate
class_name = 'Knowledge'

result = client.query.get(class_name, ["meta { count }"])

# Retrieving count from the result
count = client.query.aggregate(class_name).with_meta_count().do()
count = count['data']['Aggregate'][class_name][0]['meta']['count']
print(count)

# print(f"The total number of objects in the class '{class_name}' is {count}.")