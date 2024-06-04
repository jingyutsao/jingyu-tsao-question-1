# -*- coding: utf-8 -*-
"""Reverse words
1. Input: English or Chinese
2. The space between words will be kept in the output
"""

import pandas as pd

# Define the function to reverse words
def reverse_words(sentence):
    if any(ord(char) > 127 for char in sentence):
        # If the sentence contains non-ASCII characters, assume it's Chinese
        words = list(sentence)
        reversed_words = words[::-1]
        reversed_sentence = "".join(reversed_words)
    else:
        # Otherwise, treat it as an English sentence
        words = sentence.split()
        reversed_words = words[::-1]
        reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

def process_file(file_path):
    inputs = []
    results = []

    with open(file_path, 'r', encoding="utf-8") as file:
        test_inputs = file.read().splitlines()

        # Generate outputs
        test_outputs = [reverse_words(sentence) for sentence in test_inputs]

        # Create a DataFrame
        df = pd.DataFrame({
            "Input": test_inputs,
            "Output": test_outputs
        })
            
    return df
