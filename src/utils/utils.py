from openai import OpenAI
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


def write_dotenv(api_key: str, model: str):
    """
        Writes the API key and model to the .env file.

        Args:
                api_key (str): The API key to write to the .env file.
                model (str): The model to write to the .env file.
        """
    with open(".env", "w") as f:
        f.write(f"API_KEY={api_key}\n")
        f.write(f"MODEL={model}\n")


def llm_call(prompt: str, system_prompt: str = "", model="deepseek-chat", parameters: dict = None, role="user") -> str:
    """
    Calls the model with the given prompt and returns the response.

    Args:
        prompt (str): The user prompt to send to the model.
        system_prompt (str, optional): The system prompt to send to the model. Defaults to "".
        model (str, optional): The model to use for the call.

    Returns:
        str: The response from the language model.
    """
    if parameters is None:
        parameters = {
            "temperature": 0.7,
            "max_tokens": 4096,
            "top_p": 1.0,
        }
    try:
        client = OpenAI(api_key=os.environ["API_KEY"])
        messages = [{"role": role, "content": prompt}]
        response = client.messages.create(
            model=model,
            system=system_prompt,
            messages=messages,
            **parameters
        )
        return response.content[0].text
    except Exception as e:
        print(f"Error calling API: {e}")
        return ""


def extract_xml(text: str, tag: str) -> str:
    """
    Extracts the content of the specified XML tag from the given text. Used for parsing structured responses 

    Args:
        text (str): The text containing the XML.
        tag (str): The XML tag to extract content from.

    Returns:
        str: The content of the specified XML tag, or an empty string if the tag is not found.
    """
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1) if match else ""
