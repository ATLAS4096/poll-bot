#Corey's Program 1.2
#Adding message response system

#---the cake is a lie---#
import time
import tweepy
import json
from credentials import *

# Initialize and authenticate
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Quick Reference User ID's
atlas = 868201158224912385
dad = 866075606663876608
corey = 868679500854317056

# STANDARD FUNCTIONS (1.0)
# Tweet something
def tweet(msg):
    try:
        status = api.update_status(msg)
    except tweepy.error.TweepError:
        pass

# Send someone a direct message
def message(user, msg):
    api.send_direct_message(user_id = user, text = msg)

# Read the most recent message
def read():
    incoming = api.direct_messages(count = 1, full_text = True)
    for i in incoming:
        textTemp = i.text
        senderTemp = i.sender_id
    info = [textTemp, senderTemp]
    return info

# QUEING SYSTEM
queue = []

# Send something with up to 3 arguements into Queue
def push(tgt, contents, other): #tgt = 0 for tweet, or target's name for message. #contents = message. #other = placeholder.
    arguements = [tgt, contents, other]
    queue.append(arguements)

#Look at the first item in the Queue without removing it.
def peek():
    return queue[0]

# Take the first thing out of the Queue to do something with it.
def get():
    item = queue[0]
    queue.pop(0)
    return item

# Determine the nature of the first thing in the queue and tweet it or message it to a specific person.  Won't run if there are no items in the Queue.
def act():
    if len(queue) > 0:
        toSend = get()
        if toSend[0] == 0:
            tweet(toSend[1])
        else:
            message(toSend[0], toSend[1])

# Act multiple times.  Stops when and if the Queue runs out.
def acts(repeats):
    i = 0
    while i < repeats:
        act()
        i = i + 1

# MESSAGE RESPONSE
# Save the most recent message
def listen():
    mostRecent = 0
    while True:
        if mostRecent != read():
            mostRecent = read()
            print mostRecent
            push(mostRecent[1], "Cloudy skies...", 0)


# TESTING
