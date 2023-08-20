import requests
from agents.marketing_agent import AGENT_CONFIG, BASE_URL, API_KEY

HEADERS = {
    'X-API-Key': API_KEY
}

def agent_id_decorator(func):
    """ 
    A decorator to capture the agent_id returned by a function 
    and pass it as an argument to another function.
    """
    def wrapper(*args, **kwargs):
        agent_id = func(*args, **kwargs)
        
        # Ensure that the agent_id is valid before passing it to another function
        if agent_id is not None:
            create_agent_run(agent_id)
        else:
            print("Error: Invalid agent_id.")
    
    return wrapper

@agent_id_decorator
def create_agent(agent_config: dict) -> int:
    """
    Create an agent using a predefined body payload.

    Returns:
    - int: The agent_id of the created agent.
    """
    url = f"{BASE_URL}/api/v1/agent"
    response = requests.post(url, headers=HEADERS, json=agent_config)
    response_json = response.json()
    if response.status_code != 200:
        print("Error:", response.json())
    
    return response_json.get("agent_id")

def create_agent_run(agent_id: int) -> int:
    """
    Create a run for the agent using the provided agent_id.

    Args:
    - agent_id (int): The ID of the agent for which the run should be created.

    Returns:
    - int: The run_id of the created run.
    """
    url = f"{BASE_URL}/api/v1/agent/{agent_id}/run"
    response = requests.post(url, headers=HEADERS, json={})
    response_json = response.json()
    if response.status_code != 200:
        print("Error:", response.json())
    
    # Extract and return the run_id from the response
    return response_json.get("run_id")


def retrieve_run_resources(run_id: int) -> dict:
    """
    Retrieve the resources of a given run using its run_id.

    Args:
    - run_id (int): The ID of the run for which resources should be fetched.

    Returns:
    - dict: The resources of the given run.
    """
    url = f"{BASE_URL}/api/v1/agent/resources/output"
    payload = {"run_ids": [run_id]}
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code != 200:
        print("Error:", response.json())
    return response.json()




# Usage:
agent_id = create_agent(AGENT_CONFIG)
print(agent_id)
run_id = create_agent_run(agent_id)
if run_id:
    resources = retrieve_run_resources(run_id)
    print(resources)
else:
    print("Failed to obtain a valid run ID.")
resources = retrieve_run_resources(run_id)
print(resources)