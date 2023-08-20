import weaviate
import os
import openai
from tqdm.auto import tqdm
from time import sleep
from uuid import uuid4
import tiktoken
from langchain.text_splitter import TokenTextSplitter

OPENAI_API_KEY = ''
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")
embed_model = "text-embedding-ada-002"


def setup_weaviate(auth_key, url):
    auth_config = weaviate.AuthApiKey(api_key=auth_key)
    client = weaviate.Client(auth_client_secret=auth_config, url=url)
    return client


def split_text_into_chunks(text):
    text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=10)
    input_chunks = text_splitter.split_text(text)
    return input_chunks


def create_embeddings(texts):
    res = openai.Embedding.create(input=texts, engine=embed_model)
    for record in res['data']:
        embeds = record['embedding']
    return embeds


def store_in_weaviate(client, input_chunks):
    final_chunks = [{
        "id": str(uuid4()),
        "text": input_chunks[i],
        "chunk": i,
        "knowledge_name": "knowledge",
        "embeds": create_embeddings(input_chunks[i]),
    } for i in range(len(input_chunks))]

    # Uncomment this if you need to create a new class in Weaviate
    '''
    class_obj = {
        "class": "test",
        "vectorizer": "text2vec-openai",
    }
    client.schema.create_class(class_obj)
    '''

    vector_ids = []
    with client.batch as batch:
        for chunk in final_chunks:
            data_object = {key: value for key, value in chunk.items() if key != "id" and key != 'embeds'}
            vector_ids.append(chunk["id"])
            batch.add_data_object(data_object, "Knowledge", uuid=chunk["id"], vector=chunk["embeds"])

    # Verify if embeddings are stored
    class_name = 'Knowledge'
    count = client.query.aggregate(class_name).with_meta_count().do()
    count = count['data']['Aggregate'][class_name][0]['meta']['count']
    print(f"The total number of objects in the class '{class_name}' is {count}.")


def main(text, auth_key, url):
    client = setup_weaviate(auth_key, url)
    input_chunks = split_text_into_chunks(text)
    store_in_weaviate(client, input_chunks)


if __name__ == '__main__':
    response_json = "Your text here..."
    weaviate_auth_key = "Your Weaviate Auth Key..."
    weaviate_url = "Your Weaviate URL..."
    main(response_json, weaviate_auth_key, weaviate_url)
