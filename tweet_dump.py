"""Run this file to dump the tweets from twitter

If you see a bunch of {"error": 401} lines, it's because you haven't created
the credentials correctly.
"""

import sys
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = ""
consumer_secret = ""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = ""
access_token_secret = ""


class FileWritingListener(StreamListener):
    """ A listener writes tweets that are received from the stream.
    """

    def __init__(self, filename):
        super(FileWritingListener, self).__init__()
        self.filename = filename

    def _log(self, di):
        with open(self.filename, "a") as f:
            print(di, file=f)
        return True

    def on_data(self, data):
        return self._log(data.strip())

    def on_error(self, status):
        self._log({"error": status})

if __name__ == '__main__':
    l = FileWritingListener(sys.argv[1])
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['IPL'])
