from mastodon import Mastodon
import feedparser
from pathlib import Path
import sys

cdf = feedparser.parse('http://rawdataserver.com/CDB/rss')
tsfile = Path('/home/mastodon/deathbot/lastitem')
tsfile.touch()
lastupdated = tsfile.read_text()

if lastupdated == cdf.entries[0].published:
        sys.exit()
else:
        dead = cdf.entries[0].title
        deadlink = cdf.entries[0].links[0].href

        masto = Mastodon("", #keys go here in the order they go idk look it up
                "",
                '',
                api_base_url="" #url is whatever instance your bot is on
        )

        masto.toot('ACTUAL CELEBRITY DEATH ANNOUNEMENT\n\n' + dead + '\n\n' + deadlink)

        tsfile.write_text(cdf.entries[0].published)
