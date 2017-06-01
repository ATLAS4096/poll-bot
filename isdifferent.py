#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isDifferent(firstFile, secondFile, debug=False):

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
    print isDifferent(first, second, debug=True)

if __name__ == "__main__":
    main()