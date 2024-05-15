# src/summarizer.py
from langchain.llms import OpenAI
from config import OPENAI_API_KEY

def summarize_data(data, columns):
    # Convert the data into a string format suitable for summarization
    data_str = "\n".join([", ".join(map(str, row)) for row in data])
    prompt = f"Summarize the following data:\nColumns: {', '.join(columns)}\nData:\n{data_str}"

    # Initialize the language model
    llm = OpenAI(api_key=OPENAI_API_KEY)
    summary = llm(prompt)
    
    return summary
