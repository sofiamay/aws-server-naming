import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
# import lemmatize
from lemmatize import process_word




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
                server_names.add(process_word(word, words_suffix, server_names))

    with open('data/final_word_list.txt', 'w') as f:
        for item in server_names:
            f.write("%s\n" % item)

    return server_names


if __name__ == "__main__":
    main()

# Demonology 
