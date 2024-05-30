import sys
import os


def countBytes(fileName):
    f = open(fileName, "r")
    return os.path.getsize(fileName)


def countLines(fileName):
    f = open(fileName, "r", encoding="utf8")
    num_lines = sum(1 for i in f)
    return num_lines


if __name__ == "__main__":
    args = sys.argv[1:]
    # print(args)
    if len(args) == 0:
        print("You have not provided any option. To understand the possible options, use the flag '--help'")
    else:
        flag = args[0]
        if flag == "--help":
            print("\nThe following options are available in the WC tool:\n\n"
                  "\n-c   -->   Counts the number of bytes of a given file"
                  "\n-l   -->   Counts the number of lines in the given file"
                  "\n-w   -->   Counts the number of words in the given file"
                  "\n-m   -->   Counts the number of characters in the given file"

                  "\n\nNote: You need to provide the file name after the chosen option, and make sure that the file "
                  "is in the same directory as your pwd\n")
        elif flag == "-c":
            try:
                fileName = args[1]
                fileBytes = countBytes(fileName)
                print(fileBytes, fileName)
            except Exception as err:
                print("You're required to give a file name. Either there is no name given, or the given file isn't "
                      "present in your pwd")
        elif flag == "-l":
            try:
                fileName = args[1]
                fileLines = countLines(fileName)
                print(fileLines, fileName)
            except Exception as err:
                print("You're required to give a file name. Either there is no name given, or the given file isn't "
                      "present in your pwd")
        else:
            print("Unknown, so far")
