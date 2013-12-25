#!/usr/bin/python
"""This Map is written using Python iterators and generators for better performance."""

import sys, os

def read_input(file):
    for line in file:
        #delete spaces from line
	    line = line.strip()
	    # split the line into words
        yield line.split()

def getFileName():
    # I use configuration variables of hadoop to determine
    # The name of the file that Map is processing
	if 'map_input_file' in os.environ:
		return os.environ['map_input_file'].split("/")[-1]
	else:
		return 'none'


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    try:
        for words in data:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is 1
        # Before printing I remove some useless characters
            for word in words:
                word = filter(lambda x: x not in "\n|~()!;.,-\'\#_\"{}[]*$@%^&",word)                          
                if word :
	 		print '%s%s%s' % (word.strip("\n"), separator, getFileName().strip("\n"))
    except:
        pass
if __name__ == "__main__":
    main()
