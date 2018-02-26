#!/usr/bin/python2
# -*- coding: utf-8 -*-

import re
import sys
import csv
from tqdm import tqdm

dictionary = []
document = ''

def parse_dictionary():
    global dictionary

    # https://www.mdbg.net/chinese/dictionary?page=cc-cedict
    with open('cedict_1_0_ts_utf-8_mdbg.txt') as f:
        for line in f:
            if re.match("^#", line):
                continue
            m = re.search('^(.*) (.*) \[(.*)\] /(.*)/', line)
            if re.match("\w", m.group(1)) or re.match("%", m.group(1)):
                continue
            dictionary.append([m.group(1), m.group(2), m.group(3), m.group(4), 0, ''])

def load_document():
    global document

    with open('input.txt', 'r') as myfile:
        document = myfile.read().replace('\n', '')

def write_csv():
    with open('output.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for word in dictionary:
            if word[4] > 0:
                csvwriter.writerow([word[0], str(word[4]), word[2], word[3], word[4]])

def count_words():
    word_count = len(dictionary)
    for word_num in tqdm(range(0, word_count)):
        dictionary[word_num][4] = document.count(dictionary[word_num][0])

def main():

    parse_dictionary()
    load_document()
    count_words()
    write_csv()


if __name__ == "__main__":

    main()