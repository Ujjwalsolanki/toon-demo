import json
from toon import encode
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

file_path = 'data.json'

def print_simple_token_table(data_no_toon: dict, data_with_toon: dict) -> None:
    """
    Prints token usage data in a simple, formatted console table 
    using only built-in Python string methods.
    """
    
    # 1. Define the data rows and header labels
    data = [
        ("Prompt Tokens", data_no_toon.prompt_tokens, data_with_toon.prompt_tokens),
        ("Completion Tokens", data_no_toon.completion_tokens, data_with_toon.completion_tokens),
        ("Total Tokens", data_no_toon.total_tokens, data_with_toon.total_tokens),
    ]
    
    # Define column widths for consistent spacing
    WIDTH_A = 25  # For the metric name
    WIDTH_B = 15  # For the number columns

    # 2. Print the Header
    header = (
        f"{'Output':<{WIDTH_A}}"
        f"{'Without TOON':^{WIDTH_B}}"
        f"{'With TOON':^{WIDTH_B}}"
    )
    separator = "-" * (WIDTH_A + 2 * WIDTH_B)
    
    print("\n## 📊 Token Usage Comparison")
    print(separator)
    print(header)
    print(separator)
    
    # 3. Print the Data Rows
    for metric, no_toon_val, with_toon_val in data:
        row = (
            f"{metric:<{WIDTH_A}}"  # Left-align metric name
            f"{no_toon_val:^{WIDTH_B}}" # Center-align number
            f"{with_toon_val:^{WIDTH_B}}" # Center-align number
        )
        print(row)
        
    print(separator)

def run_comparison():
    try:
        with open(file_path, 'r') as f:
            # This loads the JSON content directly into a Python object (dict/list)
            data_object = json.load(f)
            
        encoded_data = encode(data_object)


        client = OpenAI() # Initialize your LLM client

        SYSTEM_PROMPT = (
            "You are an expert AI assistant that answers questions based ONLY on the provided USER DATA. "
            f"USER DATA: {data_object}"
        )

        USER_QUERY = "Which user is interested in 'coding' and 'cricket'?"

        response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_QUERY}
            ]
        )

        print("*"*25)
        print(f'Output without using toon {response.choices[0].message.content}')
        print("*"*25)

        usage_data_without_toon = response.usage

        SYSTEM_PROMPT = (
            "You are an expert AI assistant that answers questions based ONLY on the provided USER DATA. "
            f"USER DATA: {encoded_data}"
        )

        USER_QUERY = "Which user is interested in 'coding' and 'cricket'?"

        response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_QUERY}
            ]
        )

        print("*"*25)
        print(f'Output using toon {response.choices[0].message.content}')
        print("*"*25)
        

        usage_data_with_toon = response.usage

        print_simple_token_table(usage_data_without_toon, usage_data_with_toon)

        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: File content is not valid JSON.")

if __name__ == "__main__":
    run_comparison()