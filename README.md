
# Asana-GPT Chatbot

Asana-GPT Chatbot is a Python script that allows you to chat with your Asana workspace using the GPT language model. It uses the Asana API to download project data and creates an index using the GPTSimpleVectorIndex class to query the workspace.

## Installation

To use the script, you will need Python 3.6 or later installed on your system. You will also need an OpenAI API key and an Asana API token. You can get an OpenAI API key [here](https://beta.openai.com/signup/) and an Asana API token [here](https://developers.asana.com/docs/personal-access-token).

1. Clone the repository:

    ```
    git clone https://github.com/daveey/asana-gpt.git
    ```

2. Install the required packages:

    ```
    cd asana-gpt
    pip install -r requirements.txt
    ```

## Usage

To use the script, run the following command:

```
python asana_gpt.py --asana-token <ASANA_TOKEN> \
                  --workspace <WORKSPACE_ID> \
                  --openai-key <OPENAI_API_KEY> \
                  --chat
```

Replace `<ASANA_TOKEN>` with your Asana API token, `<WORKSPACE_ID>` with the ID of your Asana workspace, and `<OPENAI_API_KEY>` with your OpenAI API key.

You can use the `--query` option to ask the chatbot a question and get an answer:

```
python chatbot.py --asana-token <ASANA_TOKEN> --workspace <WORKSPACE_ID> --openai-key <OPENAI_API_KEY> --query "What are my tasks for today?"
```

You can also use the `--chat` option to chat with the chatbot interactively:

```
python chatbot.py --asana-token <ASANA_TOKEN> --workspace <WORKSPACE_ID> --openai-key <OPENAI_API_KEY> --chat
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
