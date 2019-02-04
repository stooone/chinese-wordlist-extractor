#!/usr/bin/python2
# -*- coding: utf-8 -*-
#coding: utf-8

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
            m = re.search('^(.*) (.*) \[(.*)\] /(.*)/', line, re.UNICODE)
            dictionary.append([m.group(2), m.group(3), m.group(4), 0, ''])


def load_document():
    global document

    with open('input.txt', 'r') as myfile:
        document = myfile.read().replace('\n', '')


def write_csv():
    global dictionary

    with open('output.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for word in dictionary:
            if word[3] > 0:
                csvwriter.writerow([word[0], str(word[3]), word[1], word[2]])


def count_words():
    global dictionary

    word_count = len(dictionary)
    for word_num in tqdm(range(0, word_count)):
        dictionary[word_num][3] = document.count(dictionary[word_num][0])


def custom_cmp(a, b):
    if len(b[0].decode("utf-8")) == 1 and len(a[0].decode("utf-8")) != 1:
        return -1
    elif len(a[0].decode("utf-8")) == 1 and len(b[0].decode("utf-8")) != 1:
        return 1
    else:
        if a[3] > b[3]:
            return -1
        else:
            return 1


def sort_words():
    global dictionary

    dictionary.sort(custom_cmp)



def main():
    parse_dictionary()
    load_document()
    count_words()
    sort_words()
    write_csv()


if __name__ == "__main__":
    main()
