import feedparser

my_feeds = [
'http://reddit.com/r/realestate/.rss']

keywords = ['agent', 'agents', 'home buying', 'diy', 'online', 'real estate']

score_dictionary = {}
for my_feed in my_feeds:
    f = feedparser.parse(my_feed)
    for entry in f['entries']:
        entry_score = 0
        for keyword in keywords:
            entry_score += entry['summary'].count(keyword)
            score_dictionary['%s : %s' % (entry['title'], entry['link'])] = entry_score

score_threshold = 3
filtered_dictionary = {key: value for key, value in score_dictionary.items() if value >= score_threshold}

sorted_dictionary = sorted(filtered_dictionary.items(), key=lambda x: x[1],reverse=True)

import pprint
pprint.pprint(sorted_dictionary)
