"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function analyze_sentence(text) that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # TODO: implement function logic
    char_count = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()
    return (char_count, word_count, contains_python)

if __name__ == "__main__":
    # TODO: read sentence from input, call function, and print results
    text = input("Enter a sentence: ")
    result = analyze_sentence(text)
    char_count, word_count, contains_python = result

    print(f"Character count: {char_count}")
    print(f"Word count: {word_count}")
    print(f"Contains 'Python': {contains_python}")