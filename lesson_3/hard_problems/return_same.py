def first():
    return {
        'prop1': "hi there",
    }

def second():
    return   #this will automatically end the function, so it will never return the dictionary
    {
        'prop1': "hi there",
    }

print(first()) #prints dict
print(second()) #prints none