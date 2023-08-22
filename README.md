# 🏴‍☠️⚡SIMBAD : Synergistic Integration of Marketing with Bot-driven Acquisition and Data-driven decisions [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://simbad.streamlit.app/) [![Vercel](http://therealsujitk-vercel-badge.vercel.app/?app=therealsujitk-vercel-badge)](https://ai-fy-chat-3x5q.vercel.app/)


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

## Technologies Used

- **Streamlit**: Our choice for building an interactive and user-friendly interface.
  
- **OpenAI**: The backbone of our conversational agent, leveraging models such as `gpt-3.5-turbo` to craft intelligent, human-like responses.
  
- **DuckDuckGoSearchRun**: Integrated to help our chatbot in pulling accurate information from the web, making its responses even more relevant.
  
- **Langchain Agents & Tools**: These frameworks facilitate the efficient and versatile operations of our agent.

---


## Building Agents in SIMBAD

In the SIMBAD system, agents act as smart entities that perform tasks using a combination of AI models, such as those from OpenAI, and other data retrieval tools.

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

## Conclusion

**SIMBAD** is not just another tool; it's the future of precision marketing. As technology propels marketing to new horizons, our solution stands as a beacon, guiding professionals towards unprecedented success. The era of generic targeting is past; the future is **SIMBAD**.

---

## Bonus

- **Expansion Roadmap**: We envision adding features like multilingual support and broadening data source integrations.
  
- **Community Connect**: Open to contributions! Fork, tailor, and send a pull request.
  
- **Adaptability**: SIMBAD's architecture allows for easy adaptability to various industries. Dive into the code and customize as your needs dictate!
