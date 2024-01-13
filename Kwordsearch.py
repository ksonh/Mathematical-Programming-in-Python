##
## Program searches for keywords in a file and prints the lines containing 
## one of the keywords, accepting command-line arguments to execute the program 
## such as "python Kwordsearch.py -max 10 -k keywords.txt input.txt", which prints 
## the first ten lines of input.txt containing one of the keywords from keywords.txt.
## Designed by: Kenneth Hanson.
## 

from sys import argv
import sys

def main():
    max_lines = -1
    keyword_file = ""
    input_file = ""

    #Parses command-line arguments.
    if len(argv) < 4 or argv[1] not in ("-k", "-max") or len(argv) < 4:
        usage()

    for i in range(1, len(argv) - 2):
        if argv[i] == "-k":
            keyword_file = argv[i + 1]
        elif argv[i] == "-max":
            max_lines = int(argv[i + 1])

    if not keyword_file or max_lines is None:
        usage()

    #This assigns the last argument 
    #in the argv list to the input file.
    input_file = argv[-1]

    #Loads keywords from file.
    keywords = loadKeywords(keyword_file)

    #Opens and reads the input file.
    with open(input_file, 'r') as infile:
        count = 0
        line = infile.readline()
        while line != "" and (max_lines == -1 or count < max_lines):
            words_found = contains(line, keywords)
            if words_found:
                print(f"Line {count + 1}: {line.strip()} (Keywords: {', '.join(words_found)})")
                print()
                count += 1
            line = infile.readline()

## Prints usage message to the console when 
## command-line arguments cannot be used.
#
def usage():
    #Prints output as standard error when usage() is called.
    print("Usage: python search.py [-max n] -k keywordfile file", file=sys.stderr)
    exit()

## Reads keywords from keyword_file and returns
## the keywords in a form of a list.
# @param keyword_file the file containing the keywords.
# @return list of keywords from file.
def loadKeywords(keyword_file):
    with open(keyword_file, 'r') as file:
        return [keyword.strip().lower() for keyword in file.readlines()]

## Determines if a line from a file contains
## the keywords specified.
# @param line the line from the file.
# @param keywords the list of keywords to check for.
# @return list of keywords in line.
def contains(line, keywords):
    line_lower = line.lower()
    return [kw for kw in keywords if kw in line_lower]

if __name__ == "__main__":
    main()