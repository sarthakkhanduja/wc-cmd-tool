import os
import argparse
import sys


def countBytes(file):
    if file == sys.stdin:
        return len(sys.stdin.read())
    else:
        return len(file.read().encode('utf-8'))


def countLines(file):
    num_lines = sum(1 for i in file)
    return num_lines


def countWords(file):
    data = file.read()
    words = data.split()
    return len(words)


def countChar(file):
    chars = 0
    for line in file:
        chars += len(line) + 1
    return chars


def process_file(file):
    if file == '-':
        return sys.stdin
    else:
        return open(file, "r", encoding="utf8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple word count tool using Python")
    parser.add_argument("-c", help="Calculates the size of the file, in bytes", action="store_true")
    parser.add_argument("-l", help="Calculates the number of lines in the file", action="store_true")
    parser.add_argument("-w", help="Calculates the number of words in the file", action="store_true")
    parser.add_argument("-m", help="Calculates the number of characters in the file", action="store_true")

    parser.add_argument("fileName", nargs='?', default='-', help="The name of the file to process")

    args = parser.parse_args()

    if args.c:
        # if args.fileName == '-':
        #     print(countBytes(process_file(args.fileName)))
        # else:
        #     print(countBytes(process_file(args.fileName)), args.fileName)
        size = countBytes(process_file(args.fileName))
        print(size, args.fileName)

    if args.l:
        if args.fileName == '-':
            print(countLines(process_file(args.fileName)))
        else:
            print(countLines(process_file(args.fileName)), args.fileName)

    if args.w:
        if args.fileName == '-':
            print(countWords(process_file(args.fileName)))
        else:
            print(countWords(process_file(args.fileName)), args.fileName)

    if args.m:
        if args.fileName == '-':
            print(countChar(process_file(args.fileName)))
        else:
            print(countChar(process_file(args.fileName)), args.fileName)

    if not(args.m or args.w or args.l or args.c) and args.fileName:
        if args.fileName == '-':
            print(countChar(process_file(args.fileName)), countLines(process_file(args.fileName)), countWords(process_file(args.fileName)))
        else:
            print(countChar(process_file(args.fileName)), countLines(process_file(args.fileName)), countWords(process_file(args.fileName)), args.fileName)