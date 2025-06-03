MADLIBS = {
    "Do you {} your {} {} {}? That's hilarious!" : [0, 1, 2, 3],
    "The {} {} {}s {} over the lazy {}" : [1, 2, 0, 3, 2],
    "The {} {} {}s up to Joe's {} turtle": [2, 3, 0, 1]
}

WORDS = ['verb', 'adjective', 'noun', 'adverb']
inputs = {}
args = []
for word in WORDS:
    inputs[word] = input(f"Enter a {word}: ")
    args.append(inputs[word])

for madlib, order in MADLIBS.items():
    print(madlib.format(*[args[i] for i in order]))
