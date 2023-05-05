import os
import openai

# Set the OpenAI organization ID and API key
openai.organization = "org-MZ6FUtTkktH1kVeWEDOejr9b"
openai.api_key = os.getenv("OPENAI_API_KEY")

class IkigAI_Agent:
    def __init__(self, agent_info):
        self.agent_info = agent_info

    def discover_purpose(self):
        """
        Discover the purpose of an AI agent and align its actions accordingly
        within the Autodidactic AI framework.

        Returns:
        - A dictionary containing the discovered purpose and related information.
        """
        # Define the prompt for discovering purpose
        prompt = (f"AI agent information:\n"
                  f"Name: {self.agent_info['agent_name']}\n"
                  f"Type: {self.agent_info['agent_type']}\n"
                  f"Capabilities: {', '.join(self.agent_info['capabilities'])}\n"
                  f"\nWhat is the core purpose of this AI agent and how should it align its actions accordingly?")

        # Use ChatGPT to generate a response to the prompt
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=100
        )

        # Extract the generated text from the response
        purpose_text = response.choices[0].text.strip()

        # Return the discovered purpose
        return {
            "purpose": purpose_text
        }

# Example usage
if __name__ == "__main__":
    agent_info = {
        "agent_name": "ExampleAgent",
        "agent_type": "nlp",
        "capabilities": ["language_generation", "question_answering"]
    }
    agent = IkigAI_Agent(agent_info)
    purpose = agent.discover_purpose()
    print(purpose)
