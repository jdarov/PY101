def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    #if statement checking length
    #if len(dot) != 4: return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break  #return False, if a number isn't in range than the whole ip address is not valid

    return True