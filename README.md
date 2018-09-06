# celebdeaths

i got tired of bofa.lol making up celebrity deaths so i wrote some scripts to check some feeds of celebrity deaths and toot them if it finds any

celebdeathbot.py checks the venerable celebritydeathbeeper rss feed
tmzdeathbot.py looks for tmz articles with "dead", "dies", or "death" in them

requires a recent enough version of Python 3 to have pathlib, feedparser, and Mastodon. should be able to pip3 install feedparser and mastodon if not idk i cant really support this

this isnt really ready to run and go you'll need to put your credentials in the code. im mostly putting this up as a reference for others and so i have a backup in case something happens. 

i have these bots run on a cron every minute thusly:

```cron
* * * * * /usr/bin/python3 /home/mastodon/deathbot/celebdeathbot.py
* * * * * /usr/bin/python3 /home/mastodon/deathbot/tmzdeathbot.py
```

oh also from the tmz rss thing, note that all TMZ content is:

```
Copyright 2018 TMZ. The contents of this headlines and excerpts feed are available for limited commercial distribution. You may repost this feed to your site provided you link back to the original story, do not edit the material and do not remove this copyright notice.
```

no edits are made to the materials. headlines and links to TMZ are provided in the output as provided by the rss feed.
