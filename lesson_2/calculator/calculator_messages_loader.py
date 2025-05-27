import json

def calc_messages(language_code='en'):
    
    """Function that returns the nested dictionary as a new dictionary in the JSON File"""
    
    with open('calculator_messages.json', 'r', encoding='utf-8') as file:
        calc_messages = json.load(file)
    return calc_messages.get(language_code, calc_messages['en'])

def get_calc_msg(calc_messages, key):
    
    """A helper function to return the message values from given key in single dict"""
    
    return calc_messages.get(key, f'Missing translation: {key}')