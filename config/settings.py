import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constant import MODEL  # e.g. 'mistral'

load_dotenv()

# Ollama doesn’t need a real key, but client requires one
api_key = os.getenv("OPENAI_API_KEY", "ollama")
# Ollama’s OpenAI-compatible endpoint
base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

# FULL model_info to satisfy Autogen >=0.4.7 validator
MODEL_INFO_FOR_OLLAMA = {
    "id": MODEL,
    "type": "chat.completions",
    "family": "mistral",            # required
    "provider": "ollama",           # optional but nice

    "input": {
        "format": "text",
        "token_window": 32768,
        "supports_streaming": True,
        "supports_json_mode": True,
        "supports_function_calling": False,
        "supports_image_input": False,
    },
    "output": {
        "max_output_tokens": 4096,
    },
    "function_calling": {
        "enabled": False,
        "parallel_tool_calls": False,
    },
    "vision": {
        "enabled": False,
        "max_input_pixels": 0,
    },
    "json_output": {
        "enabled": True,
    },
    "prompt_cache": {"enabled": False},
    "tool_use": {"enabled": False},
}

def get_model_client():
    print(f">>> Using MODEL={MODEL} via {base_url}")
    return OpenAIChatCompletionClient(
        model=MODEL,
        api_key=api_key,
        base_url=base_url,
        model_info=MODEL_INFO_FOR_OLLAMA,
    )
