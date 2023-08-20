# config.py

# Agent configuration
AGENT_CONFIG = {
    "name": "Competition Screener",
    "description": "Identify the market leaders and their Value Propositions",
    "goal": ["Identify the market leaders for {target_product} and their Value Propositions"],
    "agent_workflow": "Goal Based Workflow", 
     "constraints": [
        "If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.",
        "Ensure the tool and args are as per current plan and reasoning",
        "Exclusively use the tools listed under \"TOOLS\"",
        "REMEMBER to format your response as JSON, using double quotes (\"\") around keys and string values, and commas (,) to separate items in arrays and objects. IMPORTANTLY, to use a JSON object as a string in another JSON object, you need to escape the double quotes."
    ],
    "instruction": [
        "Inform me about the latest information about the list of Most popular {target_product}, add the link to the website that you used",
        "Identify the Value Proposition, Weaknesses and Stregths of each most popular {target_product} in the list. Add a link to your information source. ",
        "Write for each leading {target_product} a separate file with a JSON Format. REMEMBER to format your response as JSON, using double quotes (\"\") around keys and string values, and commas (,) to separate items in arrays and objects. IMPORTANTLY, to use a JSON object as a string in another JSON object, you need to escape the double quotes."    
    ],
     "tools": [
        {
           "name": "File Toolkit",
           "tools": ["Read File","Write File"]
        },
        {
          "name": "GoogleSerp"
        }
    ],
    "iteration_interval": 500,
    "model": "gpt-4",
    "max_iterations": 100,
    "schedule": null  
    
}

BASE_URL = "https://app.superagi.com"
API_KEY = "yourapikey"


#bf2b13a0-c5d3-403f-a887-ac8849b8304b

