import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun


st.sidebar.success("Select an agent above.")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/zlaabsi/simbad/backend/Home.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("🔎 SIMBAD : Synergistic Integration of Marketing with Bot-driven Acquisition and Data-driven decisions")

#st.markdown("#🔎 SIMBAD : Synergistic Integration of Marketing with Bot-driven Acquisition and Data-driven decisions")
#st.sidebar.header("SIMBAD")



st.markdown(
"""
AARRR - Unleash the Future of Marketing with AI-Enhanced Pirate Metrics!

Dive deep into micro-segmentation effortlessly, delivering pinpointed ads and AI-crafted landing pages. 
Plus, watch as our advanced autonomous agents research and refine, ushering in the era of self-optimizing funnels. 
Elevate your marketing game with intelligence with SIMBAD.
"""

"""
We're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
"""
)