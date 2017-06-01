#!/usr/bin/python

debug = True

def isDifferent(firstFile, secondFile):

    file = open(firstFile, "r")
    firstContent = file.read()
    file.close()

    if debug: print "First:"
    if debug: print firstContent

    file = open(secondFile, "r")
    secondContent = file.read()
    file.close()

    if debug: print "Second:"
    if debug: print secondContent

    if firstContent != secondContent:
        if debug: print "Different."
        return True
    else:
        if debug: print "Same."
        return False

# For testing

def main():
    first = "poll.json"
    second = "poll.json"
    return isNewer(first, second)

if __name__ == "__main__":
    main()