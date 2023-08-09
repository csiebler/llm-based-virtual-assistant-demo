# llm-based-virtual-assistant-demo

This is a simple demo for an LLM-based virtual assistant, using Azure OpenAI Service.

First, install the requirements:
```
pip install -r requirements.txt
```

Then create an `.env` with the following content:
```
AZURE_OPENAI_ENDPOINT=https://xxxxxx.api.cognitive.microsoft.com/
AZURE_OPENAI_KEY=xxxxx
AZURE_OPENAI_VERSION=2023-07-01-preview
```

Lastly run the script:
```
python bot.py
```
