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

    # iterate through words in message
    for word in words:

        # make word lowercase to compare
        lowered_word = word.lower()

        # look through words in banned list
        for s in banned:

            # if banned word is in the word in messge
            if s in lowered_word:
                print("*" * len(s), end='') # print asterisks
                print(lowered_word[len(s):len(lowered_word)], end=' ') # print rest of word to avoid losing info (commas, letters, etc)
                break # go back to beginning of loop

        # if word is not in banned, print it
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

