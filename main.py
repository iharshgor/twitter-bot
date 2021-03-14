#!/usr/bin/env python

import tweepy
import logging
from config import create_api
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f'Processing tweet id {tweet.id}')
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error(f'Error on fav {e}', exc_info=False)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error(f'Error on fav and retweet {e}', exc_info=False)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['en'],  is_async=True)


if __name__ == '__main__':
    main(['#Python'])
