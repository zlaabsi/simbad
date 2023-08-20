# config.py

# Agent configuration
AGENT_CONFIG = {
    "name": "SPEC for LP/AD",
    "description": "Create specification to generate Landing Pages and Ads for micro-segments",
    "goal": ["Create a specification of required elements for a Performance Ad and a Landing Page, so i can use it to generate them for micro-segments"],
    "agent_workflow": "Goal Based Workflow", 
    "constraints": [
        "If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.",
        "Ensure the tool and args are as per current plan and reasoning",
        "Exclusively use the tools listed under \"TOOLS\"",
        "No user assistance",
        "REMEMBER to format your response as JSON, using double quotes ("") around keys and string values, and commas (,) to separate items in arrays and objects. IMPORTANTLY, to use a JSON object as a string in another JSON object, you need to escape the double quotes."
    ],
    "instruction": [
        "Define a List of required components for a performance Ad and remember these as \"simbad_spec_ad_v1\"" ,
        "Write the result of the previous step to a file called  \"simbad_spec_ad_v1\"",
        "Define a List of required components for a landing page and remember these as \"simbad_spec_lp_v1\"",
        "Write the result of the previous step to a file called  \"simbad_spec_lp_v1\""
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
    "schedule": null  
}

BASE_URL = "https://app.superagi.com"
API_KEY = "yourapikey"


#bf2b13a0-c5d3-403f-a887-ac8849b8304b
