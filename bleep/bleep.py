# uses txt file as argument
# be sure to use python 3
from sys import argv

# check to see if user is using program properly
if len(argv) != 2:
    print("Usage: python bleep.py dictionary")
    exit(1)

# create empty set to store banned words
banned = list()

def load(dictionary):

    # open dictionary of banned words
    dictionary = open(argv[1], "r")

    # read through dictionary and
    # put each word in dictionary into banned
    for line in dictionary:
        banned.append(line.rstrip("\n"))

    # close dictionary
    dictionary.close()


def main():

    # load list of banned words
    load(argv[1])

    # take in message
    print("What message would you like to censor?")
    message = input()

    # split message into list of words to compare
    words = message.split()

    for word in words:
        lowered_word = word.lower()

        for s in banned:
            if s in lowered_word:
                print("*" * len(s), end='')
                print(lowered_word[len(s):len(lowered_word)], end=' ')
                break

            else:
                continue

        else:
            print(word, end=' ')

    # compare words in message to banned words
    # need to check for cases of 
    # for word in words:

    #     # lowercase word to compare to banned words
    #     censor = word.lower()

    #     # replace banned words in messages to asterisks
    #     if any(strg in banned for censor):
    #         print("*" * len(word), end=' ')

    #     # print words that aren't banned
    #     else:
    #         print(word, end=' ')

    # print new line
    print()


if __name__ == "__main__":
    main()

