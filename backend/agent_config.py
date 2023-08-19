# config.py

# Agent configuration
AGENT_CONFIG = {
    "name": "Marketing Specialist",
    "description": "Become a Marketing Specialist for Micro Targeting based on ChatGPT4",
    "goal": ["Become a Marketing Specialist for Micro Targeting based on ChatGPT4"],
    "agent_workflow": "Goal Based Workflow", 
    "constraints": [
        "If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.",
        "Ensure the tool and args are as per current plan and reasoning",
        "Exclusively use the tools listed under \"TOOLS\"",
        "No user assistance",
        "REMEMBER to format your response as JSON, using double quotes ("") around keys and string values, and commas (,) to separate items in arrays and objects. IMPORTANTLY, to use a JSON object as a string in another JSON object, you need to escape the double quotes."
    ],
    "instruction": [
        "Use GPT4 to explain the key success factors for a high converting micro-targeting campaign",
        "Use GPT4 to ask the 5 most important Questions to generate a high converting micro-targeting campaign",
        "Use GPT4 to explain the key success factors for a Marketeer to understand a given Market and build the leading Service/Product",
        "Use GPT4 to summarize the key psychological concept to influence customer decisions and Neurolinguistic Programmation",
        "Use GPT4 to generate a blueprint for any marketeer to run a high conversion Micro-targeting campaign, write a file"
    ],
     "tools": [
        {
           "name": "File Toolkit",
           "tools": ["Read File","Write File"]
        }
    ],
    "iteration_interval": 500,
    "model": "gpt-4",
    "max_iterations": 50,
    "schedule": {
        "start_time": "2023-08-14 21:32:00",
        "recurrence_interval": "2 Minutes",
        "expiry_runs": 2,
        "expiry_date": None
    }
}

BASE_URL = "https://app.superagi.com"
API_KEY = "yourapikey"


#bf2b13a0-c5d3-403f-a887-ac8849b8304b