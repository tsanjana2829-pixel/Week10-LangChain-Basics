# Week 10 – LangChain Basics

## Task
Building LLM Applications using LangChain Prompt Templates and Chains.

## Project contents
- `langchain_chatbot.py` – command-line College Assistant chatbot using LangChain and local Ollama.
- `notebook/Week10_LangChain_Basics.ipynb` – notebook version with setup and example chain.
- `dataset/` – sample prompts, user queries, chatbot responses, and chain results.
- `requirements.txt` – Python dependencies.

## Requirements
1. Install Python 3.10+.
2. Install and start Ollama.
3. Download the model: `ollama pull llama3.2`
4. Install packages: `py -m pip install -r requirements.txt`
5. Run: `py langchain_chatbot.py`

If your computer uses `python` instead of `py`, replace `py` with `python`.

## Notes
This project uses a local Ollama model. The first response may take some time while the model loads.
