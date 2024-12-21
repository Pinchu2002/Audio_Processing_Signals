# Ensure you have installed the library:
# pip install indic-transliteration

from indic_transliteration import sanscript

def is_hindi(word):
    # Check if the majority of characters fall in Devanagari range
    # This is a heuristic; adjust as needed.
    for ch in word:
        if '\u0900' <= ch <= '\u097F':
            return True
    return False

def is_english(word):
    # Check if all characters are in English alphabet range
    # Adjust logic if you have punctuation, numbers, etc.
    return all((ch.isalpha() and ch.isascii()) for ch in word)

def transliterate_english_to_hindi(word):
    # Here we assume word is in ITRANS format for simplicity.
    # If your words are normal English words like "Hello" and you want to 
    # just map them phonetically, you must define that mapping.
    # For demonstration, let's assume the word is already in ITRANS form.
    return sanscript.transliterate(word, sanscript.ITRANS, sanscript.DEVANAGARI)

input_file = 'input.txt'
output_file = 'transliterated_output.txt'

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        words = line.strip().split()
        new_words = []
        for w in words:
            if is_hindi(w):
                # Already Hindi, leave as is
                new_words.append(w)
            elif is_english(w):
                # Transliterate English word
                # If the word isn't in ITRANS, you must define a mapping.
                # Example: Let’s say you treat the English word as if it’s ITRANS:
                # "namaste" in ITRANS is "namaste", transliterates to "नमस्ते"
                # For a random English word "Hello", you need a custom mapping.
                
                # For demo, directly transliterate (assuming word is in ITRANS):
                transliterated = transliterate_english_to_hindi(w.lower())
                new_words.append(transliterated)
            else:
                # If it doesn't fit either category well, just leave it unchanged
                new_words.append(w)
        
        f_out.write(' '.join(new_words) + '\n')
