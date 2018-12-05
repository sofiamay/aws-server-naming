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

def main():
    #read file
    word_list = read_file("data/wordList")
    # generates a list of suffixes and their lengths. E.g. [ ['ing',3], ['ed',2],...]
    suffixes = read_file("data/suffixes", lambda x: re.compile(r'\w*%s\b' % x) )

    # stem words and remove stopwords
    stop_words = set(stopwords.words("english"))
    server_names = []

    for word in word_list:
        if word not in stop_words:
            if not matches_regexes(word, suffixes):
                server_names.append(word)

    print(server_names[0:50])
    return server_names


if __name__ == "__main__":
    main()

# Demonology 
