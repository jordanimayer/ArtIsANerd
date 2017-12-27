# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:36:50 2017

@author: Jordan Mayer, mayer15@purdue.edu

A very simple Twitter bot that replies to @Queen__Arthur
and calls her a nerd. Ignores retweets. Might ignore replies
in the future.

Mostly intended as a learning experience for the developer.

Utilizes tweepy and Molly White's twitter bot framework.
"""

# Copyright (c) 2015–2016 Molly White
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
nerd = "@Queen__Arthur nerd"  # the text to tweet


# SteamListener to listen to Art's tweets
class ArtStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if not status.retweeted and ('RT @' not in status.text):
            print(status.text)

        # decode JSON data
        # tweetID = data.id
        # tweet = json.loads(data)
        # if not tweet['retweeted']:
        # reply(nerd, tweetID)

    def on_error(self, status_code):
        if status_code == 420:
            return False

def create_tweet():
    """Create the text of the tweet you want to send."""

    test = "Hello world!"
    return test

    # Replace this with your code!
    # text = "@Queen__Arthur nerd"
    # return text


def tweet(text):
    """Send out the text as a tweet"""
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)


def reply(text, reply_to):
    """Reply to Art's tweets"""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text, reply_to)
    except tweepy.error.TweepError as e:
        if (e.message == None):
            log("Error with no message")
            print("Error with no message")
        else:
            log(e.message)
            print(e.message)
    else:
        log("Tweeted in reply to " + str(reply_to) + ": " + text)
        print("Tweeted in reply to " + str(tweet.id) + ": " + "@Queen__Arthur nerd")


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)

def get_tweets():
    for status in tweepy.Cursor(api.user_timeline, screen_name='@Queen__Arthur').items():
        if not status.retweeted and ('RT @' not in status.text):
            print(status.text)


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    lastDate = datetime.datetime(2017, 12, 24, 0, 0, 0)

    allTweets = api.user_timeline(ArtID, count=100)
    tweets = []
    #print("Here")
    for tweet in allTweets:
        #print(tweet.text)
        if not tweet.retweeted and ('RT @' not in tweet.text) \
                and (tweet.created_at > lastDate) and (tweet.in_reply_to_status_id == None):
            print(tweet.text)
            #tweets.append(tweet)
            #reply("@Queen__Arthur nerd", tweet.id)

    #ArtSL = ArtStreamListener()
    #ArtStream = tweepy.Stream(auth=api.auth, listener=ArtStreamListener())
    #ArtStream.filter(follow=[Queen__Amber])
