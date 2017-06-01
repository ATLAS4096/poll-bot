#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def isDifferent(firstFile, secondFile, debug=False):

    try:
        file = open(firstFile, "r")
        firstContent = file.read()
        file.close()
    except:
        return True

    if debug: print "First:"
    if debug: print firstContent

    try:
        file = open(secondFile, "r")
        secondContent = file.read()
        file.close()
    except:
        return True

    if debug: print "Second:"
    if debug: print secondContent

    if firstContent != secondContent:
        if debug: print "Different."
        return True
    else:
        if debug: print "Same."
        return False

# For testing

# def main():
#     first = "poll.json"
#     second = "poll.json"
#     print isDifferent(first, second, debug=True)
#
# if __name__ == "__main__":
#     main()