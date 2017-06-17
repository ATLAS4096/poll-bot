#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time
import tweepy
import datetime
import tweeter

from getpoll import *
from isdifferent import *
from credentials import *

TweetItOut = True
MainLoopTimer = 120

#
# Initialize and message when the bot starts
#
def initialize():
    message = 'ATLAS poll-bot restarted...'
    recipients = [COREY, DAD]
    for recipient in recipients:
        # Send message to recipient as a direct message
        if TweetItOut: tweeter.message(recipient, message)

#
# Check a poll result and decide whether to act on it
#
def checkPoll():

    pollName = "trump-approval-poll"
    preservedPollName = "trump-approval-poll.last"
    resourceBase = 'https://elections.huffingtonpost.com/pollster/api/v2/polls/'
    pollDisplayName = "Trump Approval Rating - Gallup"
    pollReferralBase = "https://elections.huffingtonpost.com/pollster/polls/"
    pollListResource = "https://elections.huffingtonpost.com/pollster/api/v2/polls"

    pollId = findPoll(pollListResource, 'gallup')
    resource = resourceBase + pollId
    pollReferralLink = pollReferralBase + pollId

    # NBC / WSJ: nbc-wsj-<number>
    # Quinnipiac: quinnipiac-<number>
    # Gallup: gallup-<number>

    # Preserve the last polling data
    if os.path.isfile(pollName + '.json'):
        os.rename(pollName + '.json', preservedPollName + '.json')

    # Load the latest poll result
    result = getPoll(resource, pollName, saveAside=True, debug=False)

    # Compare to see if result has changed
    if isDifferent(pollName + '.json', preservedPollName + '.json', debug=True):
        message = pollDisplayName + \
            "   Approve: " + str(result["Approve"]) + \
            "   Disapprove: " + str(result["Disapprove"]) + \
            "   See: " + pollReferralLink
        print message
        if TweetItOut: tweeter.tweet(message)
    else:
        print "Not tweeting."

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
        try:
            remoteCommand = remoteCommandCheck()
            if remoteCommand == CommandExit:
                break
            else:
                processRemoteCommand(remoteCommand)
            checkPoll()
        except Exception as e:
            print "Exception in main loop: " + str(e)
        print 'Waiting ' + str(MainLoopTimer) + ' seconds.'
        time.sleep(MainLoopTimer)
    print 'Exiting...'