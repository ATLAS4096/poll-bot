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

Version = 2.0

Debug = True # Production: set to False
TweetItOut = True # Production: set to True
InitialDelayTimer = 6 # Production: set to 60 # FOR PI: wait for Wi-Fi to start on reboot
MainLoopTimer = 12 # Production set to 120

BetweenTweetTimer = 5

class Poll:
    keyword = ""
    pollName = ""
    preservedPollName = ""
    pollDisplayName = ""
    resourceBase = 'https://elections.huffingtonpost.com/pollster/api/v2/polls/'
    pollReferralBase = "https://elections.huffingtonpost.com/pollster/polls/"
    pollListResource = "https://elections.huffingtonpost.com/pollster/api/v2/polls"

gallupPoll = Poll()
gallupPoll.keyword = "gallup"
gallupPoll.pollName = "trump-approval-poll-gallup"
gallupPoll.preservedPollName = "trump-approval-poll-gallup.last"
gallupPoll.pollDisplayName = "Trump Approval Rating - Gallup"

ipsosPoll = Poll()
ipsosPoll.keyword = "ipsos"
ipsosPoll.pollName = "trump-approval-poll-ipsos"
ipsosPoll.preservedPollName = "trump-approval-poll-ipsos.last"
ipsosPoll.pollDisplayName = "Trump Approval Rating - Ipsos"

quinnipiacPoll = Poll()
quinnipiacPoll.keyword = "quinnipiac"
quinnipiacPoll.pollName = "trump-approval-poll-quinnipiac"
quinnipiacPoll.preservedPollName = "trump-approval-poll-quinnipiac.last"
quinnipiacPoll.pollDisplayName = "Trump Approval Rating - Quinnipiac"

#
# Initialize and message when the bot starts
#
def initialize():
    time.sleep(InitialDelayTimer)
    message = 'ATLAS poll-bot restarted...'
    recipients = [COREY, DAD]
    for recipient in recipients:
        # Send message to recipient as a direct message
        if TweetItOut: tweeter.message(recipient, message)

#
# Check a poll result and decide whether to act on it
#
def checkPoll(poll):
    pollId = findPoll(poll.pollListResource, poll.keyword)
    resource = poll.resourceBase + pollId
    pollReferralLink = poll.pollReferralBase + pollId

    # Gallup: gallup-<number>
    # Ipsos: ipsos-reuters-<number>
    # NBC / WSJ: nbc-wsj-<number>
    # Quinnipiac: quinnipiac-<number>

    # Preserve the last polling data
    if os.path.isfile(poll.pollName + '.json'):
        if not os.path.isfile(poll.preservedPollName + '.json'):
            os.rename(poll.pollName + '.json', poll.preservedPollName + '.json')

    # Load the latest poll result
    result = getPoll(resource, poll.pollName, saveAside=True, debug=Debug)

    # Compare to see if result has changed
    if isDifferent(poll.pollName + '.json', poll.preservedPollName + '.json', debug=Debug):
        message = poll.pollDisplayName + \
            "   Approve: " + str(result["Approve"]) + \
            "   Disapprove: " + str(result["Disapprove"]) + \
            "   See: " + pollReferralLink
        print message
        # if TweetItOut: tweeter.tweet(message)
        if TweetItOut: tweeter.pushAdd(0, message)
    else:
        print "No difference in poll, not tweeting."

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
# <>----------MAIN LOOP----------<>
#
if __name__ == "__main__":
    print "ATLAS Poll-Bot version " + str(Version)
    print "Starting..."
    initialize()
    while True:
        try:
            remoteCommand = remoteCommandCheck()
            if remoteCommand == CommandExit:
                break
            else:
                processRemoteCommand(remoteCommand)
            checkPoll(ipsosPoll)
            #time.sleep(BetweenTweetTimer) # replaced by queue
            checkPoll(gallupPoll)
            #time.sleep(BetweenTweetTimer) # replaced by queue
            checkPoll(quinnipiacPoll)

            #Queueing System
            if len(tweeter.MainQueue) > 0:
                print "Executing from Queue"
                tweeter.execute()
                time.sleep(60)
            else:
                "Nothing in queue to execute."
                tweeter.add("listen")
                time.sleep(60)

        except Exception as e:
            try:
                print e
            except Exception as inner:
                print "Could not print exception."
            print "Exception in main loop...continuing."
        print 'Waiting ' + str(MainLoopTimer) + ' seconds.'
        # time.sleep(MainLoopTimer) # replaced by queue
    print 'Exiting...'