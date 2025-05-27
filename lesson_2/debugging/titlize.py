def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            new_words.append(word.capitalize())
        else:
            new_words.append(word) #should not be nested in the if statement 

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))