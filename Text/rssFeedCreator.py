# Given a link to RSS/Atom Feed, get all posts and display them.

import feedparser
rss_feed = raw_input("Please give me the link to the rss feed you would like to view. ")
rss_feed = feedparser.parse(str(rss_feed))
print rss_feed['feed']['title']
print rss_feed.feed.subtitle
print len(rss_feed['entries'])
for post in rss_feed.entries:
    print post.title + ": " + post.link + ""
