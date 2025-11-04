"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re

def count_characters(text):
    """Count non-space characters in a string."""
    return len([ch for ch in text if not ch.isspace()])

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    return [int(num) for num in re.findall(r"\d+", text)]

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    chars = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers) if numbers else 0
    average = total / len(numbers) if numbers else 0
    return chars, words, numbers, total, average

if __name__ == "__main__":
    text = input("Enter some text: ")
    chars, words, numbers, total, average = analyze_text(text)
    print(f"Non-space characters: {chars}")
    print(f"Words: {words}")
    print(f"Numbers found: {numbers}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {average:.2f}")