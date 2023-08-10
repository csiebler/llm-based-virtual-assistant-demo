# llm-based-virtual-assistant-demo

This is a simple demo for an LLM-based virtual assistant, using Azure OpenAI Service.

## General idea

In this repo, we show how LLMs can be used to build an intent-driven chatbot, that can make API calls in the backend to perform actions on behalf of the user. To achieve this, we use `gpt-35-turbo` for performing:

- High level intent classification (into broad categories)
- Using Azure OpenAI function calling to then actually perform task, that the user wants to get done

By splitting it up, we achieve the following:

* **Scalability:** In real-world scenarios, we often want to enable users to perform 100's of tasks. Passing in 100's of OpenAI function definitions as an array into our main prompt is just not feasible, as it would be larger than our token window. Instead, classifying on the highest level as a first step is fast and does not require a lot of tokens, in fact even with 1-2k token windows we can easily give a bunch of high-level categories including a few examples. Once the top intent has been classified, we can drill down into the details using function calls. As a side effect, this also enables a simple chit-chat conversation on the top level, without requiring extra tokens.

* **Economics**: Our top level intent classifier is cheap to operate, requiring only a small amount of tokens. Therefore, even if our detailed journeys are larger (many different API calls via OpenAI function calling), we can still operate this cost-efficiently.

* **Operational benefits**: Splitting up the individual intents allows us to test and validate intent categories independently, hence allows us to identify weaknesses in our prompts and therefore independent improve individual tasks the assistant should perform.

## Running the repo

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
