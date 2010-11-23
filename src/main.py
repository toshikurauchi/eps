'''
Created on Nov 23, 2010

@author: Andrew Kurauchi
'''
import sys

def main():
    inputFileName = sys.argv[1]
    inputFile = open(inputFileName, 'r')
    for line in inputFile:
        print line,

if __name__ == '__main__':
    sys.exit(main())