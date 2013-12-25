#!/usr/bin/python
"""This Combine is written using Python iterators and generators for better performance."""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        #Map output : key \t value
        #So this thing splits key and value
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from standard input
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    for current_word, group in groupby(data, itemgetter(0)):
        fileList = {}
        count = 0
        outp = ""
        for current_word, fileName in group:
        #I am using python Dictionary(HashTable)
        #python's dictionary: {key1:value1,key2:value2,......}
        #I use as key the DocId and as value how many times
        #the word appeared in that document
            if fileList.has_key(fileName):
                count = int(fileList[fileName])
            fileList[fileName] = count + 1
        outp = outp + "|" + fileName + ":" + str(fileList[fileName])
        print "%s\t%s" % (current_word, outp.rstrip("\n"))
if __name__ == "__main__":
    main()
