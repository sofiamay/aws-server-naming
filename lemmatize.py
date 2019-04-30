# Accepts a word, a suffix contained on the word, and a list of words that have already been processed
# Returns a strong to add to the list of accepted server_names
# Return an empty string to skip over the word and NOT add to the final list
def process_word(word, suffix, server_names):
	return globals()[suffix](word, server_names)



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
    # if root word is in list, return it. Else add full word to list
    if word[0:-4] in server_names:
        return word[0:-4]
    else:
        return word

def like(word, server_names):
	# remove suffix. If root is in list, return it. Else add full word
	if word[0:-4] in server_names:
		return word[0:-4]
	else:
		return word

def less(word, server_names):
	# remove suffix. If root is in list, return it. Else add full word
	if word[0:-4] in server_names:
		return word[0:-4]
	else:
		return word
	