# ⚡ LLM Token Optimization: TOON vs. JSON Comparison

This repository contains a simple Python script to benchmark the token consumption difference between standard **JSON** and the new **TOON (Token Oriented Object Notation)** when structuring data for Large Language Model (LLM) API calls.

**Goal:** Achieve significant cost savings and faster processing times by reducing the input token count.

## 🚀 Core Concept: Why TOON?

When sending data to an LLM via a prompt, every character counts as a token (or part of one). JSON is verbose, including many tokens for formatting (`{`, `}`, `,`, `"`, newlines). TOON is a minimalist notation designed specifically to reduce this "syntactic overhead," leading to much smaller prompts.

| Feature | Standard JSON | TOON (Token Oriented) |
| :--- | :---: | :---: |
| **Token Usage** | High (Verbose) | Low (Compact) |
| **Human Readability** | Difficult for large arrays | High (Tabular/YAML-like) |
| **Best Data Type** | Any structure | Flat Arrays of Objects |

## ⚠️ Critical Finding: The Flat Data Rule

For maximum token savings, the data sent to the LLM **must be a flat structure**.

* ✅ **DO USE:** Flat arrays (e.g., a list of user objects with no nested fields).
* ❌ **DO NOT USE:** Nested JSON (objects inside objects, or arrays inside fields).

**Using TOON with nested data structures may actually increase your token count compared to standard JSON.**

## 🛠️ Project Setup

### Prerequisites

1.  Python 3.8+
2.  An OpenAI API Key (or a similar LLM provider key).

### Installation

```bash
# Install the necessary libraries
pip install openai python-toon python-dotenv
````

### Environment Variables

Set your OpenAI API key in your environment:

```bash
export OPENAI_API_KEY="YOUR_API_KEY_HERE"
```

## 💻 How to Run the Benchmark

The included Python script (`benchmark.py` - *conceptual name*) performs two identical LLM calls: one with JSON data and one with TOON-encoded data.

### Function: `run_comparison()`

The function will print a clean comparison table showing the token usage for each method.

```python
# benchmark.py (Conceptual structure)
from openai import OpenAI
import toon
# ... (rest of the setup and data)

def run_comparison():
    # ... logic to make the JSON call and get token_usage_json
    # ... logic to make the TOON call and get token_usage_toon
    
    # Print the results in a table
    print_simple_token_table(token_usage_json, token_usage_toon)
    # The print_simple_token_table function logic is included in this file.

if __name__ == "__main__":
    run_comparison()
```

## 📊 Expected Output

The console output will resemble the following token-saving comparison:

| Output | Without TOON | With TOON |
| :--- | :---: | :---: |
| Prompt Tokens | 123 | 65 |
| Completion Tokens | 45 | 20 |
| **Total Tokens** | **168** | **85** |

### Actual comparison
![Message 1](assets/Screenshot_2.png)

**Conclusion:** In this example, TOON reduced the total token usage by almost 41.30%, resulting in lower costs and faster processing.
