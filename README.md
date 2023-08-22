# 🏴‍☠️⚡SIMBAD : Synergistic Integration of Marketing with Bot-driven Acquisition and Data-driven decisions [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://simbad.streamlit.app/) [![Vercel](http://therealsujitk-vercel-badge.vercel.app/?app=therealsujitk-vercel-badge)](https://ai-fy-chat-3x5q.vercel.app/)

⚠️ **Disclaimer: we have two versions of our solution, the first on [Streamlit](https://simbad.streamlit.app/) and the second on [Vercel](https://ai-fy-chat-3x5q.vercel.app/). The first mainly uses Langchain, while the second uses SuperAGI.** ⚠️



## 🔗 [Lablab.ai Hackathon Link](https://lablab.ai/event/autonomous-agents-hackathon/next-big-tool/simbad-microtargeting-solution)

> **AARRR** - *Unleash the Future of Marketing with AI-Enhanced Pirate Metrics!*

Dive deep into micro-segmentation effortlessly, delivering pinpointed ads and AI-crafted landing pages. Watch as our advanced autonomous agents research and refine, ushering in the era of self-optimizing funnels. Elevate your marketing game with intelligence with **SIMBAD**.

Our solution is primarily aimed at performance & growth marketers and ad specialists. With SIMBAD, you can develop a comprehensive microtargeting solution that leverages data-driven insights, empowering professionals to create precise and high-converting ad campaigns.

---

## Demo

### Classic use
https://github.com/zlaabsi/simbad/assets/52045850/1741cfa5-8198-4979-8ed7-170e3c3265cd

### Using the agent's memory

https://github.com/zlaabsi/simbad/assets/52045850/7655e35f-cdcf-4208-86c7-0680d708faf1


---



## Building Agents with LangChain 🦜🔗

In the SIMBAD system, agents act as smart entities that perform tasks using a combination of AI models, such as those from OpenAI, and other data retrieval tools.

---

### Technologies Used

- **Streamlit**: Our choice for building an interactive and user-friendly interface.
  
- **OpenAI**: The backbone of our conversational agent, leveraging models such as `gpt-3.5-turbo` to craft intelligent, human-like responses.
  
- **DuckDuckGoSearchRun**: Integrated to help our chatbot in pulling accurate information from the web, making its responses even more relevant.
  
- **Langchain Agents & Tools**: These frameworks facilitate the efficient and versatile operations of our agent.

---

### 1. **Initialization**

Before creating agents, we must initialize necessary frameworks and dependencies:

```python
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
```




### 2. **Competition Screener Agent**

The Competition Screener Agent's role is to identify competitors in a given market for a particular product. The agent would likely use a combination of the AI model to interpret the user's query and data retrieval tools, like a web search tool, to pull in relevant competitor information.

#### Script Example:

```python
def competition_screener_agent(target_product, messages):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=API_KEY, streaming=True)
    search = DuckDuckGoSearchRun(name=f"Find competitors for {target_product}")
    
    competition_agent_instance = initialize_agent([search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)
    
    response = competition_agent_instance.run(messages)
    
    return response
```



### 3. **Spec Agent**

This agent's primary responsibility is to generate specifications for landing pages and ads.

#### Script Example:

```python
def spec_agent(messages):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=API_KEY, streaming=True)
    search = DuckDuckGoSearchRun(name="Search for LP/AD Spec")
    
    spec_agent_instance = initialize_agent([search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)
    
    response = spec_agent_instance.run(messages)
    
    return response
```

### 4. **Targeting Generator Agent**

This agent is built to generate micro-segments for specific products and apply pre-defined specs.

#### Script Example:

```python
def targeting_generator_agent(target_product, messages):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=API_KEY, streaming=True)
    search = DuckDuckGoSearchRun(name=f"Generate Microsegments for {target_product}")
    
    targeting_agent_instance = initialize_agent([search], llm, agent=AgentType.GOAL_BASED_WORKFLOW, handle_parsing_errors=True)
    
    response = targeting_agent_instance.run(messages)
    
    return response
```

### 5. **Running the Agents**

Once the agents are defined, they can be executed using user input.

#### Script Example:

```python
user_input = "fitness app"  # This would ideally be taken from an interface like Streamlit
messages = [{"role": "user", "content": user_input}]

spec_response = spec_agent(messages)
targeting_response = targeting_generator_agent(user_input, messages)
competition_response = competition_screener_agent(user_input, messages)

print(spec_response)
print(targeting_response)
print(competition_response)
```


These script examples provide a foundational understanding of how the agents in the SIMBAD system might be structured and how they could be utilized. The actual implementation might differ based on design choices, additional functionalities, and system constraints.

---

## Running the Application

1. **Environment Preparation**: Ensure all dependencies are available. A popular method is using `pip`:
   ```bash
   pip install streamlit openai langchain duckduckgo-search
   ```

2. **Repository Access**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **API Key Configuration**: Open the Streamlit interface and on the sidebar, key in your OpenAI API credentials.

4. **Launch the Streamlit App**:
   ```bash
   streamlit run <filename>.py
   ```

5. **Engage with the Chatbot**: Enter your desired target product and observe as the bot intricately crafts its replies.

---
---

## Building with SuperAGI 🤖

SuperAGI provides an extensive framework for constructing intelligent agents. SIMBAD, leveraging this framework, orchestrates multiple agents to achieve data-driven marketing decisions with unparalleled precision.

### Agent Creation Script

Through SuperAGI's robust API, agents are easily defined, configured, and deployed. Here's an illustrative configuration:

```python
# Agent configuration
AGENT_CONFIG = {
    "name": "Marketing Specialist",
    "description": "Become a Marketing Specialist for Micro Targeting based on ChatGPT4",
    "goal": ["Become a Marketing Specialist for Micro Targeting based on ChatGPT4"],
    "agent_workflow": "Goal Based Workflow", 
    "constraints": [
        "If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.",
    ...
}

BASE_URL = "https://app.superagi.com"
API_KEY = "yourapikey"
```

This agent, titled "Marketing Specialist," is designed to immerse itself in the nuances of micro-targeting via the prowess of GPT-4.


---

### Integration with Weaviate for Knowledge Embeddings

The integration with Weaviate, a state-of-the-art vector database, empowers the SIMBAD solution to store and query high-dimensional embeddings with ease. The following steps outline how textual data from the agent's output is split, transformed into embeddings, and stored in Weaviate :

1. **Setting up Weaviate**: A connection to the Weaviate instance is established.
2. **Text Splitting**: Large texts are broken down into digestible chunks.
3. **Embedding Creation**: These chunks are then processed into embeddings.
4. **Storage**: Embeddings are stored in Weaviate for rapid retrieval.

#### 1. **Setting Up Weaviate Connection**
Establish a connection with the Weaviate instance by providing the necessary authentication key and URL.

```python
import weaviate

def setup_weaviate(auth_key, url):
    auth_config = weaviate.AuthApiKey(api_key=auth_key)
    client = weaviate.Client(auth_client_secret=auth_config, url=url)
    return client
```

#### 2. **Text Splitting**
To manage the token limits imposed by models, we split larger texts into smaller chunks using the Langchain Text Splitter.

```python
from langchain.text_splitter import TokenTextSplitter

def split_text_into_chunks(text):
    text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=10)
    input_chunks = text_splitter.split_text(text)
    return input_chunks
```

#### 3. **Creating Embeddings with OpenAI**
For each text chunk, an embedding is generated using OpenAI.

```python
import openai

OPENAI_API_KEY = 'Your_OpenAI_API_Key'
openai.api_key = OPENAI_API_KEY
embed_model = "text-embedding-ada-002"

def create_embeddings(texts):
    res = openai.Embedding.create(input=texts, engine=embed_model)
    embeddings = [record['embedding'] for record in res['data']]
    return embeddings
```

#### 4. **Storing Embeddings in Weaviate**
The generated embeddings are then stored in Weaviate's 'Knowledge' vector DB, each associated with its chunk of text.

```python
from uuid import uuid4

def store_in_weaviate(client, input_chunks):
    embeddings = create_embeddings(input_chunks)
    final_chunks = [{
        "id": str(uuid4()),
        "text": input_chunk,
        "embedding": embedding,
    } for input_chunk, embedding in zip(input_chunks, embeddings)]
    
    with client.batch as batch:
        for chunk in final_chunks:
            batch.add_data_object(chunk, "Knowledge", uuid=chunk["id"])

    # Verify if embeddings are stored
    count = client.query.aggregate('Knowledge').with_meta_count().do()['data']['Aggregate']['Knowledge'][0]['meta']['count']
    print(f"The total number of objects in the 'Knowledge' class is {count}.")
```

#### 5. **Main Function**
Integrating all the aforementioned functions for execution.

```python
def main(text, auth_key, url):
    client = setup_weaviate(auth_key, url)
    input_chunks = split_text_into_chunks(text)
    store_in_weaviate(client, input_chunks)

if __name__ == '__main__':
    response_json = "Your agent's textual output..."
    weaviate_auth_key = "Your Weaviate Auth Key"
    weaviate_url = "Your Weaviate URL"
    main(response_json, weaviate_auth_key, weaviate_url)
```





---

### Technologies Used

1. **SuperAGI**: The underlying framework for creating and orchestrating intelligent agents.
2. **ChatGPT-4**: Utilized as the core AI model to power the intelligent responses and actions of our agents.
3. **Weaviate**: A state-of-the-art vector database for rapid and efficient data storage and retrieval.
4. **Langchain Text Splitter**: A tool used to split larger textual content into manageable pieces.
5. **OpenAI**: Used for embedding creation, a critical step before storage in Weaviate.

### Running the Application

To start the SIMBAD solution, follow these steps:

1. Clone the repository.
2. Set up your environment variables including `OPENAI_API_KEY`, `WEAVIATE_AUTH_KEY`, and `WEAVIATE_URL`.
3. Run the initial setup scripts to ensure all data sources are prepared.
4. Start the main application using the command `streamlit run simbad_app.py`.


---


## Conclusion

**SIMBAD** is not just another tool; it's the future of precision marketing. As technology propels marketing to new horizons, our solution stands as a beacon, guiding professionals towards unprecedented success. The era of generic targeting is past; the future is **SIMBAD**.

---

## Bonus

- **Expansion Roadmap**: We envision adding features like multilingual support and broadening data source integrations.
  
- **Community Connect**: Open to contributions! Fork, tailor, and send a pull request.
  
- **Adaptability**: SIMBAD's architecture allows for easy adaptability to various industries. Dive into the code and customize as your needs dictate!
