import nltk
import re
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords




# return array of lines (words) in file
# Optionally perform function(line) on each line in fine
def read_file(filename, func=None):
    with open(filename, "r", newline=None) as file:
        array = []
        for line in file:
            line = line.rstrip()
            if func:
                line = func(line)
            array.append(line)
        return array

# boolean: returns true if a word matches at least one regex in a list
def matches_regexes(word, regexes):
    for regex in regexes:
        if regex.match(word):
            return True
    return False

# Each of these functions contains instructions for how to deal with a different suffix

def able(word):
    # Delete suffix, if result is already in the list, return that word. Else return full word
    if word[0:-4] in server_names:
        return word[0:-4]
    else:
        return word

def ed(word):
    # if root word is in list, return that word, else return full word
    if word[0:-2] in server_names:
        return word[0:-2]
    else:
        return word

def er(word):
    # if root word is in list, return it. Else add full word to list
    if word[0:-2] in server_names:
        return word[0:-2]
    else: return word

def es(word):
    vowels = ["a","e","i","o","u"]
    # ends in vowel + consonant, remove the "s"
    if (word[-3] not in vowels) and (word[-4] in vowels):
        return word[0:-1]
    # ends in "ies," replace with "y"
    else if word[-3] == "i":
        return word[0:-3] + "y"
    # ends in "ves," replace with "f"
    else if word[-3] == "v":
        return = word[0:-3] + f
    # else, remove "es"
    else:
        word = word[0:-2]

def est(word):
    # if ends in "iest" transform to "y" and return
    if word[-4] == "i":
        return word[0:-4] + "y"
    # if root word is in list, return that word, else return full word
    if word[0:-3] in server_names:
        return word[0:-3]
    else:
        return word



# global variables
server_names = {}



# def main():
#     #read file
#     word_list = read_file("data/wordList")
#     # generates a list of suffixes and their lengths. E.g. [ ['ing',3], ['ed',2],...]
#     suffixes = read_file("data/suffixes", lambda x: re.compile(r'\w*%s\b' % x) )

#     # stem words and remove stopwords
#     stop_words = set(stopwords.words("english"))
#     server_names = []

#     for word in word_list:
#         if word not in stop_words:
#             if not matches_regexes(word, suffixes):
#                 server_names.append(word)

#     with open('data/final_word_list.txt', 'w') as f:
#         for item in server_names:
#             f.write("%s\n" % item)

#     return server_names


if __name__ == "__main__":
    main()

# Demonology 
