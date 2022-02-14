import json

from difflib import get_close_matches

a = json.load(open("C:/Users/KHUSHI/Desktop/data.json"))

def b(word):
    word = word.lower()
    if word in a:
        return a[word]
    elif word.title() in a:
        return a[word.title()]
    elif word.upper() in a:
        return a[word.upper()]
    elif len(get_close_matches(word, a.keys())) > 0:
        print("Did you %s instead of" %get_close_matches(word, a.keys())[0])
        choose = input("press y for yes or n for no:")
        if choose == "y":
            return a[get_close_matches(word , a.keys())[0]]
        elif choose == "n":
            return("Please check your spelling.")
        else:
            return("You have entered wrong input, please enter just y or n.")
    else:
        print("Please check you spelling")

word = input("Enter a word:")
meaning = b(word)
if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)
