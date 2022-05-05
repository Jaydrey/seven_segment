import re
import json
from typing import Dict
import sys

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

def show_words(word_list: list[str])->None:
    for index, word in enumerate(word_list):
        print(word)
        if index%10==0 and index!=0:
            # press enter to continue
            input("Click enter to show the other 10")

def acceptable_words(word_list: list[str]):
    accepted_words = [word for word in word_list if not re.search(r"[{DISALLOWED_LETTERS}]", word)]
    return {
        "number_of_words": len(accepted_words),
        "list of words": show_words(accepted_words),
    }

def main():
    if len(sys.argv)>1:
        word_list = dict_to_array(word_dict)
        if sys.argv[1]=="-accepted":
            accepted = acceptable_words(word_list)
            print(f"Words that can be displayed by the 7-segment display")
            print(accepted)
        elif sys.argv[1] == "-longest":
            longest_word, length = longest_seven_segement_word(word_list)
            print(f"The longest words to be displayed by the seven segment display are {length} charcaters long")
            input("Click enter to see them")
            print(longest_word)

    else:
        raise Exception(
            "You haven't provided the mode of service.\nArgumnets to provide:\n1. -accepted\t returns \
            words that can be displayed by the 7-segment display\n\
                2. -longest\t returns longest english word displayed in 7-segment display")

if __name__ == '__main__':
    main()


