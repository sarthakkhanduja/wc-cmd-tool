import os
import sys
import argparse


def countBytes(fileName):
    return os.path.getsize(fileName)


def countLines(fileName):
    f = open(fileName, "r", encoding="utf8")
    num_lines = sum(1 for i in f)
    return num_lines


def countWords(fileName):
    f = open(fileName, "r", encoding="utf8")
    data = f.read()
    words = data.split()
    return len(words)


def countChar(fileName):
    chars = 0
    with open(fileName, 'r', encoding='utf-8') as file:
        for line in file:
            chars += len(line) + 1
    return chars


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple word count tool using Python")
    parser.add_argument("-c", help="Calculates the size of the file, in bytes", action="store_true")
    parser.add_argument("-l", help="Calculates the number of lines in the file", action="store_true")
    parser.add_argument("-w", help="Calculates the number of words in the file", action="store_true")
    parser.add_argument("-m", help="Calculates the number of characters in the file", action="store_true")

    parser.add_argument("fileName", help="The name of the file to process")

    args = parser.parse_args()

    if args.c:
        print(countBytes(args.fileName), args.fileName)

    if args.l:
        print(countLines(args.fileName), args.fileName)

    if args.w:
        print(countWords(args.fileName), args.fileName)

    if args.m:
        print(countChar(args.fileName), args.fileName)

    if not(args.m or args.w or args.l or args.c) and args.fileName:
        print(countLines(args.fileName), countWords(args.fileName), countChar(args.fileName), args.fileName)