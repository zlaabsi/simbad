# config.py

# Agent configuration
AGENT_CONFIG = {
    "name": "Generating 40 Micro-Segments",
    "description": "Create 40 micro-segments for a fitness App",
    "goal": ["Create a List of 40 micro-segments to target for a fitness App with all information needed to create an Ad and a Landing Page per Micro-Segment"],
    "agent_workflow": "Goal Based Workflow", 
    "constraints": [
        "If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.",
        "Ensure the tool and args are as per current plan and reasoning",
        "Exclusively use the tools listed under \"TOOLS\"",
        "No user assistance",
        "REMEMBER to format your response as JSON, using double quotes ("") around keys and string values, and commas (,) to separate items in arrays and objects. IMPORTANTLY, to use a JSON object as a string in another JSON object, you need to escape the double quotes."
    ],
    "instruction": [
        "Define a List of required components for a performance Ad and List of required components of a Landing Page",
        "Generate a full list with all of the 40 micro segments for a fitness App, with the required components for each  of them"            
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
