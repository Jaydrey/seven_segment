import re
import json
from typing import Dict

# letters we won't allow to display in the seven segment display
DISALLOWED_LETTERS = "gkmqwxyzio"

# reading from a json file containing a dictionary of emglish letters
with open("words_dictionary.json") as word_json:
    word_dict = json.load(word_json)

# transforming the extracted dictionary into a list containing words
def dict_to_array(dictionary: Dict[str, int])-> list[str]:
    word_list = [ word_key for word_key in dictionary]
    return word_list

# called to sort the list of words 
# it returns a list of words whose length are the same but the longest 
# from all the other words in the list
def get_longest_corresponding_words(words: list[str]):
    sorted_words = sorted(words, key=lambda x: len(x))
    longest_len = len(sorted_words[-1])
    corresponding_words = [word for word in sorted_words if len(word)==longest_len]
    return corresponding_words, longest_len

# main function that returns the longest acceptable words 
def longest_seven_segement_word(word_list: list[str]):
    current_longest_word: str = ""
    corresponding_word_len:list[str] = []
    for word in word_list:
        if re.search(rf"[{DISALLOWED_LETTERS}]", word):
            continue
        if  len(word)>len(current_longest_word):
            current_longest_word = word
        if len(word)==len(current_longest_word):
            corresponding_word_len.append(word)
        
    other_longest_word, length = get_longest_corresponding_words(corresponding_word_len)

    return ("\n".join(other_longest_word), length)
if __name__ == '__main__':
    
    word_list = dict_to_array(word_dict)
    long_words, length = longest_seven_segement_word(word_list)
    print(f"The longest words to be displayed by the seven segment display are {length} charcaters long")
    input("Click enter to see them")
    print(long_words)


