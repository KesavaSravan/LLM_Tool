# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f4hl8Qw5UVgacPcVZsxTi-RVzFib4qvB


!pip install transformers torch gradio
"""
# Import necessary libraries
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import gradio as gr

# Load pre-trained model and tokenizer (e.g., GPT-2)
model_name = "gpt2"  # You can replace it with any other model, like "facebook/opt-125m"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate a response based on the user prompt
def generate_response(prompt: str, max_length: int = 150):
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate the response using the model
    outputs = model.generate(
        inputs['input_ids'],
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_p=0.92,
        temperature=0.7
    )

    # Decode the generated output and return the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Gradio interface function
def prompt_to_response(prompt: str):
    return generate_response(prompt)

# Gradio UI with input box and a display area for the output
iface = gr.Interface(
    fn=prompt_to_response,
    inputs="text",
    outputs="text",
    title="LLM-Based Tool",  # Title of the web interface
    description="Enter a prompt to generate a response using GPT-2 or other pre-trained models. You can test with general text generation, Q&A, or summarization prompts."
)

# Launch the Gradio app
iface.launch()