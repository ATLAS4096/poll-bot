#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time
import tweepy
import datetime

from getpoll import *
from isdifferent import *
from credentials import *

MainLoopTimer = 30

#
# Initialize and message when the bot starts
#
def initialize():
    message = 'ATLAS poll-bot restarted...'
    recipients = [COREY, DAD]
    for recipient in recipients:
        # Send message to recipiate as a direct message
        # TODO: add Twitter messaging
        0

#
# Check a poll result and decide whether to act on it
#
def checkPoll():

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

        # TODO: send this text as a tweet
    else:
        print "Should not tweet."

#
# Remote command handling
#

CommandNone = 0
CommandExit = 999

def remoteCommandCheck():
    # TODO: add Twitter check
    return CommandNone

def processRemoteCommand(command = CommandNone):
    # TODO: add command handling
    return command

#
# Main
#
if __name__ == "__main__":
    print "Starting..."
    initialize()
    while True:
        remoteCommand = remoteCommandCheck()
        if remoteCommand == CommandExit:
            break
        else:
            processRemoteCommand(remoteCommand)
        checkPoll()
        print 'Waiting ' + str(MainLoopTimer) + ' seconds.'
        time.sleep(MainLoopTimer)
    print 'Exiting...'