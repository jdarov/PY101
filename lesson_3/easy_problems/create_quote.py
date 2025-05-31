famous_words = "seven years ago..."

concatonate_quote = 'Four score and ' + famous_words

def prepend_quote(quote):
    prepend = 'Four score and '
    return prepend + famous_words

print(concatonate_quote)
print(prepend_quote(famous_words))