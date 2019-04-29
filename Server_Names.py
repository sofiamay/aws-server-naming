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

# returns a the suffix as a string if a word matches at least one regex in a list
# each suffix has the form [regex, string]
def matches_regexes(word, suffixes):
    for suffix in suffixes:
        if suffix[0].match(word):
            return suffix[1]
    return ""

# # Each of these functions contains instructions for how to deal with a different suffix

def able(word, server_names):
    # Delete suffix, if result is already in the list, return that word. Else return full word
    if word[0:-4] in server_names:
        return word[0:-4]
    else:
        return word

def ed(word, server_names):
    # if root word is in list, return that word, else return full word
    if word[0:-2] in server_names:
        return word[0:-2]
    else:
        return word

def er(word, server_names):
    # if root word is in list, return it. Else add full word to list
    if word[0:-2] in server_names:
        return word[0:-2]
    else: return word

def es(word, server_names):
    vowels = ["a","e","i","o","u"]
    # ends in vowel + consonant, remove the "s"
    if (word[-3] not in vowels) and (word[-4] in vowels):
        return word[0:-1]
    # ends in "ies," replace with "y"
    elif word[-3] == "i":
        return word[0:-3] + "y"
    # ends in "ves," replace with "f"
    elif word[-3] == "v":
        return word[0:-3] + "f"
    # else, remove "es"
    else:
        word = word[0:-2]

def est(word, server_names):
    # if ends in "iest" transform to "y" and return
    if word[-4] == "i":
        return word[0:-4] + "y"
    # if root word is in list, return that word, else return full word
    if word[0:-3] in server_names:
        return word[0:-3]
    else:
        return word

def ification(word, server_names):
    # ignore word
    return ""

def ization(word, server_names):
    return ""

def tional(word, server_names):
    return ""

def tioning(word, server_names):
    return ""

def ation(word, server_names):
    return ""

def tion(word, server_names):
    # delete "ion." If root not a word, return full word
    if word[0:-3] in server_names:
        return word[0:-3]
    else:
        return word

def fully(word, server_names):
    return ""

def ify(word, server_names):
    return ""

def ian(word, server_names):
    return ""

def ic(word, server_names):
    # if root is a word, return it. Else return full word
    if word[0:-2] in server_names:
        return word[0:-2]
    else:
        return word

def ing(word, server_names):
    # remove suffix
    return word[0:-3]

def ion(word, server_names):
    # replace suffix with "e"
    return word[0:-3] + "e"

def ism(word, server_names):
    return ""

def ist(word, server_names):
    return ""

def ity(word, server_names):
    return ""

def logy(word, server_names):
    # if root word is in list, return it. Else add full word to list
    if word[0:-4] in server_names:
        return word[0:-4]
    else:
        return word

def ally(word, server_names):
    return ""

def ly(word, server_names):
    # if root word is in list, return it. Esle add full word to list
    if word[0:-2] in server_names:
        return word[0:-2]

    else:
        return word

def ment(word, server_names):
    return ""

def ness(word, server_names):
    return ""

def ship(word, server_names):
    # if root word is in list, return it. Esle add full word to list
    if word[0:-4] in server_names:
        return word[0:-4]
    else:
        return word





def main():
    #read file
    word_list = read_file("data/wordList")
    # generates a list of suffixes, each a tuple of the form [regex, string]
    suffixes = read_file("data/suffixes", lambda x: [re.compile(r'\w*%s\b' % x), x] )

    # stem words and remove stopwords
    stop_words = set(stopwords.words("english"))
    server_names = set()

    for word in word_list:
        if len(word) < 12 and word not in stop_words:
            words_suffix = matches_regexes(word, suffixes)
            if not words_suffix:
                # word has no suffix. Append as is to the final list
                server_names.add(word)
            else:
                # word has suffix. Process before appending
                final_word = globals()[words_suffix](word, server_names)


    with open('data/final_word_list.txt', 'w') as f:
        for item in server_names:
            f.write("%s\n" % item)

    return server_names


if __name__ == "__main__":
    main()

# Demonology 
