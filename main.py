import json
from difflib import get_close_matches as gcm


data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    autoCorrect = gcm(word, data.keys(), cutoff=0.8)
    if word in data:
        return data[word]
    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(autoCorrect) > 0:
        yn = input(
            "did you mean %s insted!! if yes enter y,enter n if No: " % autoCorrect[0])
        if yn == "y":
            return data[autoCorrect[0]]
        elif yn == "n":
            return "The word doesnt exist"
        else:
            return "We cannot understand your query"
    else:
        return "sorry Enter the correct word"


word = input("Enter the word: ")


output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
