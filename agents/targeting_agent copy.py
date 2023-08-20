# config.py

# Agent configuration
AGENT_CONFIG = {
    "name": "Targeting Generator",
    "description": "Generate Microsegments and Apply Specs previously stored ",
    "goal": ["Generate Microsegments for a {target_product} and apply Specs previously stored"],
    "agent_workflow": "Goal Based Workflow", 
    "constraints": [
        "If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.",
        "Ensure the tool and args are as per current plan and reasoning",
        "Exclusively use the tools listed under \"TOOLS\"",
        "No user assistance",
        "REMEMBER to format your response as JSON, using double quotes ("") around keys and string values, and commas (,) to separate items in arrays and objects. IMPORTANTLY, to use a JSON object as a string in another JSON object, you need to escape the double quotes."
    ],
    "instruction": [
        "Act as a Marketing expert, generate a list of 10 Micro-Segments to grow userbase of a {target_product}",
        "Use the supplied input file SIMBAD_SPEC_LP_V1.txt as a structure for generating a landing page for each of the Microsegments. Write the results to a single file for each of the Micro-Wegments. REMEMBER to format your response as JSON, using double quotes ("") around keys and string values, and commas (,) to separate items in arrays and objects. IMPORTANTLY, to use a JSON object as a string in another JSON object, you need to escape the double quotes.",
        "Use the supplied input file SIMBAD_SPEC_AD_V1.txt as a structure for generating an Ad for each of the Microsegments.  Write the results to a single file for each of the Micro-Wegments. REMEMBER to format your response as JSON, using double quotes ("") around keys and string values, and commas (,) to separate items in arrays and objects. IMPORTANTLY, to use a JSON object as a string in another JSON object, you need to escape the double quotes."
    ],
     "tools": [
        {
           "name": "File Toolkit",
           "tools": ["Read File","Write File"]
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
