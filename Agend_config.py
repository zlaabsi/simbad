# config.py

# Agent configuration
AGENT_CONFIG = {
    "name": "Aug 17 MS 2606",
    "description": "AI assistant to solve complex problems",
    "goal": ["create a photo of a cat"],
    "agent_workflow": "Goal Based Workflow", 
    "constraints": [
        "~4000 word limit for short term memory.",
        "Your short term memory is short, so immediately save important information to files.",
        "If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.",
        "No user assistance",
        "Exclusively use the commands listed in double quotes e.g. \"command name\""
    ],
    "instruction": [],
    "tools": [
        {
            "name": "DuckDuckGo Search Toolkit",
            "tools": ["DuckDuckGoSearch"]
        },
        {   
            "name": "Image Generation Toolkit",
            "tools": ["DalleImageGeneration"]
        }
    ],
    "iteration_interval": 500,
    "model": "gpt-4",
    "max_iterations": 25,
    "schedule": {
        "start_time": "2023-08-14 21:32:00",
        "recurrence_interval": "2 Minutes",
        "expiry_runs": 2,
        "expiry_date": None
    }
}

BASE_URL = "{{URL}}"
API_KEY = 'bf2b13a0-c5d3-403f-a887-ac8849b8304b'
