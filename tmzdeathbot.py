from mastodon import Mastodon
import feedparser
from pathlib import Path
import sys

cdf = feedparser.parse('http://www.tmz.com/rss.xml')
tsfile = Path('/home/mastodon/deathbot/tmzlastitem')
tsfile.touch()
lastupdated = tsfile.read_text()

for entry in cdf.entries:
        if "dead" in entry.title.lower() or "dies" in entry.title.lower() or "death" in entry.title.lower():
                if lastupdated == entry.date:
                        sys.exit()
                dead = entry.title
                deadlink = entry.link

                masto = Mastodon("", #you'll have to put your api key secret whatever here idk go look it up
                        "",
                        '',
                        api_base_url="" #instance url
                )

                masto.toot('POSSIBLE death via TMZ\n\n' + dead + '\n\n' + deadlink)

                tsfile.write_text(entry.date)
