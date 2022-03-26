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
import httpx
import httpcore

# create logger
logger = getLogger(__name__)

__author__ = 'FoxMaSk'
__all__ = ['Rss']


class Rss:

    USER_AGENT = 'FeedParserData/0.1.3 +https://framagit.org/annyong/nyuseu'

    def get_data(self, url_to_parse, bypass_bozo=False, **kwargs) -> typing.Any:
        """
        read the data from a given URL or path to a local file
        :string url_to_parse : URL of the Feed to parse
        :boolean bypass_bozo : for not well-formed URL, do we ignore or not that URL
        :return: Feeds if Feeds are well-formed
        """
        data = FeedParserDict()
        with httpx.Client(timeout=30) as client:
            logger.debug(url_to_parse)
            try:
                feed = client.get(url_to_parse)
                data = feedparser.parse(feed.text, agent=self.USER_AGENT)
                # if the feeds is not well-formed, return no data at all
                if bypass_bozo is False and data.bozo == 1:
                    data.entries = ''
                    log = f"{url_to_parse}: is not valid. Make a try by providing 'True' to 'Bypass Bozo' parameter"
                    logger.info(log)
            except httpcore.ConnectTimeout as e:
                logger.error(e)
            except httpcore.ReadTimeout as e:
                logger.error(e)
            except httpx.ConnectTimeout as e:
                logger.error(e)
            except httpx.ConnectError as e:
                logger.error(e)
            except httpx.ReadTimeout as e:
                logger.error(e)
        return data
