#Twitter Interface 1.3 - "tweeter"
#Formerly "Corey's Program"
#   Improving Messaging System.
#   Redacted Quick Reference ID's, moved to "credentials" file.
#   Renamed lots of stuff.
#   Added main queue for doing everything in one-minute intervals so to avoid Twitter's obnoxious rate-limit.

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
#[REDACTED]!    

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

# MAIN ACTION QUEUEING SYSTEM
MainQueue = []

# Put a command into the MainQueue
def add(cmd, p2=0, p3=0):
    arguments = [cmd, p2, p3]
    MainQueue.append(arguments)

# Command List
#send
#listen
#log - for debug purposes

# Execute a command from the MainQueue
def execute():
    item = MainQueue[0]
    MainQueue.pop(0)
    if item[0] == "send":
        send()
    elif item[0] == "listen":
        listen()
    elif item[0] == "log":
        log()

# Prints a message instead of running a real command
def log():
    print "Execute command triggered LOG."

# OUTBOUND QUEING SYSTEM
OutQueue = []

# Send something with up to 3 arguments into OutQueue
def push(tgt, contents, other=0): #tgt = 0 for tweet, or target's name for message. #contents = message. #other = placeholder.
    arguments = [tgt, contents, other]
    OutQueue.append(arguments)

#Look at the first item in the OutQueue without removing it.
def peek():
    return OutQueue[0]

# Take the first thing out of the OutQueue to do something with it.
def get():
    item = OutQueue[0]
    OutQueue.pop(0)
    return item

# Determine the nature of the first thing in the OutQueue and tweet it or message it to a specific person.  Won't run if there are no items in the OutQueue.
def send():
    if len(OutQueue) > 0:
        toSend = get()
        if toSend[0] == 0:
            tweet(toSend[1])
        else:
            message(toSend[0], toSend[1])

# Act multiple times.  Stops when and if the OutQueue runs out.  Currently BROKEN with Main Queue system.
def sends(repeats):
    i = 0
    while i < repeats:
        act()
        i = i + 1

# MESSAGE RESPONSE
# Save the most recent message
def listen():
    mostRecent = read()
    print mostRecent
    return mostRecent

# Save all functions since last check
def getMsgs():
    # TODO: Make getMsgs working!
    return

# TESTING
push(0, "Hi, there!")
#add("send")
while True:
    if len(MainQueue) > 0:
        execute()
        time.sleep(60)
    else:
        add("listen")