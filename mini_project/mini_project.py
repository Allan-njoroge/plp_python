import json
from difflib import get_close_matches

#function that opens the json data file
def load_dictionary():
    with open("./dictionary-data-master/data.json") as file:
        data = json.load(file)
    return data

def find_definition(word, data):
    word = word.lower()

    if word in data:
        return data[word]
    
    elif word.title() in data:
        return data[word.title()]
    
    elif word.upper() in data:
        return data[word.upper()]
    
    elif len(get_close_matches(word, data.keys())) > 0:
        suggestion = get_close_matches(word, data.keys())[0]
        confirm = input("Did you mean '%s' instead? [y/n] ")

        if confirm.lower() == "y":
            return data[suggestion];
        elif confirm.lower() == "n":
            return "The word does not exist, Kindly double check"
        else:
            return "We didn't understand you entry"

    else:
        return "The word does not exist"

#The main function
def main():
    data = load_dictionary()
    word = input("Enter a word to find its meaning: ")
    meaning = find_definition(word, data)

    if isinstance(meaning, list):
        for item in meaning:
            print(item)
    
    else:
        print(meaning)

if __name__ == "__main__":
    main()