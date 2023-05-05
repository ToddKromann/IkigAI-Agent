import requests

class IkigAI_Agent:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def discover_purpose(self, agent_info):
        """
        Discover the purpose of an AI agent and align its actions accordingly
        within the Autodidactic AI framework.

        Parameters:
        - agent_info: A dictionary containing information about the AI agent.

        Returns:
        - A dictionary containing the discovered purpose and related information.
        """
        # Define the endpoint URL for discovering purpose
        endpoint_url = f"{self.api_url}/api/discover_purpose"

        # Define the headers for the API request
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }

        # Make the API request to discover the purpose of the AI agent
        response = requests.post(endpoint_url, json=agent_info, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            result = response.json()
            return result
        else:
            # Handle the error case
            raise Exception(f"API request failed with status code {response.status_code}")

# Example usage
if __name__ == "__main__":
    # Define the API key and URL for the IkigAI-Agent plugin
    API_KEY = "your_api_key_here"
    API_URL = "http://localhost:3333"

    # Create an instance of the IkigAI_Agent class
    ikigai_agent = IkigAI_Agent(api_key=API_KEY, api_url=API_URL)

    # Define the information about the AI agent
    agent_info = {
        "agent_name": "example_agent",
        "agent_type": "nlp",
        "capabilities": ["language_generation", "question_answering"]
    }

    # Discover the purpose of the AI agent
    purpose = ikigai_agent.discover_purpose(agent_info)

    # Print the discovered purpose
    print(purpose)
