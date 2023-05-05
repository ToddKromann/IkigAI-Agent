
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration options for IkigAI-Agent

# API key for accessing the ChatGPT API (from OpenAI)
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

# API endpoint for ChatGPT (from OpenAI)
CHATGPT_API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# API key for accessing the Autodidactic AI framework's API
AUTODIDACTIC_AI_API_KEY = os.getenv("AUTODIDACTIC_AI_API_KEY")

# API endpoint for the Autodidactic AI framework's API
AUTODIDACTIC_AI_API_ENDPOINT = "https://example.com/autodidactic_ai_api"

# Other configuration options specific to IkigAI-Agent
# ...

