# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:36:50 2017

@author: Jordan Mayer, mayer15@purdue.edu

A very simple Twitter bot that replies to @Queen__Arthur
and calls her a nerd. Ignores retweets and replies.

Mostly intended as a learning experience for the developer.

Utilizes tweepy and Molly White's twitter bot framework.
"""


import os
import tweepy
import datetime
from secrets import *
from time import gmtime, strftime

# ====== Individual bot configuration ==========================
bot_username = 'ArtIsANerd'
logfile_name = bot_username + ".log"

# ==============================================================

ArtID = "2957673249"  # Art's twitter ID


class ArtStreamListener(tweepy.StreamListener):
    """
    SteamListener to listen to Art's tweets

    Currently not in use; may utilize in the future if using Raspberry Pi
    or VPS to run 24/7
    """
    def on_status(self, status):
        # Filter out retweets and replies
        if not tweet.retweeted and ('RT @' not in tweet.text) \
                and (tweet.in_reply_to_status_id is None):
            print(tweet.text)   # for testing
            # reply("@Queen__Arthur nerd", tweet.id)

    def on_error(self, status_code):
        if status_code == 420:
            return False


def reply(text, reply_to):
    """
    Reply to a tweet

    text = text of reply (must include @<user>)
    reply_to = id of status (or user) to reply to
    """

    # Send reply and log success or failure
    try:
        api.update_status(text, reply_to)
    except tweepy.error.TweepError as e:
        if (e.message is None):
            log("Error with no message")
            print("Error with no message")
        else:
            log(e.message)
            print(e.message)
    else:
        log("Tweeted in reply to " + str(reply_to) + ": " + text)

def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    """Fetch all Amber's tweets since last run and reply"""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    lastDate = datetime.datetime(2017, 12, 24, 0, 0, 0)     # Date of last run

    tweets = api.user_timeline(ArtID, count=100)     # Art's last 100 tweets
    for tweet in tweets:
        # Filter out retweets, replies, and old tweets
        if not tweet.retweeted and ('RT @' not in tweet.text) \
                and (tweet.created_at > lastDate) and (tweet.in_reply_to_status_id is None):
            print(tweet.text + "\n")    # Print tweet being replied to
            reply("@Queen__Arthur nerd", tweet.id)  # Reply to tweet

    """
    Create and filter StreamListener
    Currently not in use; may utilize in the future if using Raspberry Pi
    or VPS to run 24/7
    """
    #ArtSL = ArtStreamListener()
    #ArtStream = tweepy.Stream(auth=api.auth, listener=ArtStreamListener())
    #ArtStream.filter(follow=[ArtID])
