"""
countTxtAll.py
author: GlennGorgoth
date: Nov 4, 2020

Imports a .txt file and counts all occurances of each word. 
Returns a list of all words in ascending order of most common.
"""

from hashmap import HashMap

# Change TEXT to the path of the file you want to count
TEXT = 'WordCounter/AliceInWonderland.txt'

def clean_line(raw_line):
    '''removes all punctuation from input string and
    returns a list of all words which have a length greater than one'''
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)): # pylint: disable=C0200
        if line[index] < 'a' or line[index] > 'z':
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words

def main():
    """opens a text file, puts all words into a hashmap,
    sorts it by most common words, prints the first 15"""
    text = open(TEXT, "r")
    hm = HashMap()
    for line in text:
        words = clean_line(line)
        for word in words:
            count = hm.get(word)
            if count is None:
                hm.set(word, 1)
            else:
                hm.set(word, count + 1)
    most_common_words = hm.asc_sort()
    print("The most common words are:")
    for item in most_common_words:
        # print(item)
        print('{:<10s}{:>10d}'.format(item[1], item[0]))

if __name__ == "__main__":
    main()
