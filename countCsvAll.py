"""
countCsvAll.py
author: GlennGorgoth
date: Nov 4, 2020

Imports a .csv file and counts all occurances of each word in a given column.
Returns a list of all words in ascending order of most common.
"""

from hashmap import HashMap
import csv

# Change TEXT to the path of the file you want to count
TEXT = 'WordCounter/Survey.csv'

# Change FIELD to the name of the field/column in the csv you want to count
FIELD = 'Movies seen'

# Change OUTPUT to the name of the csv file you want to export
OUTPUT = 'results.csv'


# field names
OUTPUT_FIELDS = ['Name', 'Count']
	

def writeCSV(rows):
    with open(OUTPUT, 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(OUTPUT_FIELDS)
        write.writerows(rows)


def main():
    """opens a csv file, puts all words into a hashmap,
    sorts it by most common words, creates a new csv with results"""
    hm = HashMap()
    with open(TEXT, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            text = row[FIELD]
            print(text)
            entries = text.split(', ')
            for entry in entries:
                count = hm.get(entry)
                if count is None:
                    hm.set(entry, 1)
                else:
                    hm.set(entry, count + 1)
    most_common_words = hm.asc_sort()
    most_common_words_desc = hm.sort(-1)
    new_csv = []
    for item in most_common_words_desc:
        new_item = [item[1],item[0]]
        new_csv.append(new_item)
    print("The most common entries are:")
    for item in most_common_words:
        # print(item)
        print('{:<10s}{:>10d}'.format(item[1], item[0]))
    writeCSV(new_csv)

if __name__ == "__main__":
    main()
