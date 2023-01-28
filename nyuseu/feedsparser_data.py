# coding: utf-8
"""
   FeedParserData
"""
# std lib
from __future__ import unicode_literals
from logging import getLogger
import typing
# external lib
import feedparser
from feedparser.util import FeedParserDict
import requests
# create logger
logger = getLogger(__name__)

__author__ = 'FoxMaSk'
__all__ = ['Rss']


class Rss:

    USER_AGENT = 'FeedParserData/0.1.3 +https://git.afpy.org/foxmask/nyuseu'

    def get_data(self, url_to_parse, bypass_bozo=False, **kwargs) -> typing.Any:
        """
        read the data from a given URL or path to a local file
        :string url_to_parse : URL of the Feed to parse
        :boolean bypass_bozo : for not well-formed URL, do we ignore or not that URL
        :return: Feeds if Feeds are well-formed
        """
        data = FeedParserDict()
        # httpx does not handle url with 302 returned code o_O
        # with httpx.Client(timeout=30) as client:
        #    logger.debug(url_to_parse)
        #    try:
        #        feed = requests.get(url_to_parse)
        #        feed = client.get(url_to_parse)
        #        print(feed)
        #        print(feed.text, feed.content   )
        #        data = feedparser.parse(feed.text, agent=self.USER_AGENT)
        #        print(data)
        #        # if the feeds is not well-formed, return no data at all
        #        if bypass_bozo is False and data.bozo == 1:
        #            data.entries = ''
        #            log = f"{url_to_parse}: is not valid. Make a try by providing 'True' to 'Bypass Bozo' parameter"
        #            logger.info(log)
        #    except (httpcore.ConnectTimeout, httpcore.ReadTimeout, httpcore.ReadError,
        #            httpx.ConnectTimeout, httpx.ConnectError, httpx.ReadTimeout) as e:
        #        logger.error(e)
        logger.debug(url_to_parse)
        try:
            feed = requests.get(url_to_parse)
            data = feedparser.parse(feed.text, agent=self.USER_AGENT)
            if bypass_bozo is False and data.bozo == 1:
                data.entries = ''
                log = f"{url_to_parse}: is not valid. Make a try by providing 'True' to 'Bypass Bozo' parameter"
                logger.info(log)
        except (requests.ConnectTimeout, requests.ReadTimeout, ) as e:
            logger.error(e)

        return data
