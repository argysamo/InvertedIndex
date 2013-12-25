#!/usr/bin/python
"""This Reduce is written using Python iterators and generators for better performance."""

from itertools import groupby
from operator import itemgetter
import sys,os

def read_mapper_output(file, separator='\t'):
    try:
        for line in file:
        #every line has the following appereance:
        #word \t |DocId1:value1|DocId2:value2
            line = line.strip()
            #value is:|DocId1:value1|DocId2:value2 
            word,value = line.split(separator)
            value = value.split("|")
            value.remove("")
            #for i in value:
             #   i = i.split(":")
              #  DocId = i[0]
               # Wc = int(i[1])
            
            yield word, value
    except:
        pass
def main(separator='\t'):
    # input comes from standard input
    data = read_mapper_output(sys.stdin, separator=separator)
  
    for current_word, group in groupby(data, itemgetter(0)):
        fileList = {}
        outp = ""
        for current_word, value in group:
            for i in value:
                i = i.split(":")
                DocId = i[0]
                Wc = int(i[1])
                if fileList.has_key(DocId):
                    Wc = int(fileList.has_key(DocId)) + Wc
                fileList[DocId] = Wc
        for Key,Value in fileList.items():
            outp = outp + "|" + Key + ":" + str(Value)    
        
        print "%s%s%s" % (current_word, separator, outp.rstrip("\n"))
if __name__ == "__main__":
    main()

