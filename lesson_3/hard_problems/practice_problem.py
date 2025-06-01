PUNCTUATION = {',', '!', '.'}

def extract_unique_words(input_string):
    input_string = input_string.lower()
    for punctuation in PUNCTUATION:
        input_string = input_string.replace(punctuation, '')
    
    word_list = input_string.split()
    final_words = []
    for word in word_list:
        if word not in final_words:
            final_words.append(word)
    return final_words

input_string = "Hello, world! Hello Launch School. Python, launch, PYTHON."

print(extract_unique_words(input_string))
