import nltk
import re
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer



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

def main():
    #read file
    word_list = read_file("data/wordList")
    suffixes = read_file("data/suffixes", lambda x: re.compile(r'\w*%s\b' % x))
    test = re.compile(r'\w*ed\b')
    print(suffixes[1].match('played'))

    # stem words and remove stopwords
    stop_words = set(stopwords.words("english"))
    ps = PorterStemmer()
    server_names = []

    for word in word_list:
        if word not in stop_words:
            if ps.stem(word) != word:
                server_names.append(word)
    return server_names


if __name__ == "__main__":
    main()