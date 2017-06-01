#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time
import tweepy
import datetime

from getpoll import *
from isdifferent import *

# Main
def main():

    pollName = "trump-approval-poll"
    preservedPollName = "trump-approval-poll.last"
    resource = 'https://elections.huffingtonpost.com/pollster/api/v2/polls/gallup-27729'
    pollDisplayName = "Trump Approval Rating - Gallup"
    pollReferralLink = "https://elections.huffingtonpost.com/pollster/polls/gallup-27729"

    # NBC / WSJ: nbc-wsj-27531
    # Quinnipiac: quinnipiac-27728
    # Gallup: gallup-27729

    # Preserve the last polling data
    if os.path.isfile(pollName + '.json'):
        os.rename(pollName + '.json', preservedPollName + '.json')

    # Load the latest poll result
    result = getPoll(resource, pollName, saveAside=True, debug=False)

    # Compare to see if result has changed
    if isDifferent(pollName + '.json', preservedPollName + '.json', debug=True):
        print pollDisplayName
        print "   Approve: " + str(result["Approve"])
        print "   Disapprove: " + str(result["Disapprove"])
        print "   See: " + pollReferralLink
    else:
        print "Should not tweet."

if __name__ == "__main__":
    main()