# Hearthstone Utilities
--
*__Note:__ These utilities are not, in any way, sponsored, endorsed, or otherwise
affilitiated with Blizzard's Hearthstone: Heroes of Warcraft.*

These utilites are Python 3 scripts that allow users to play around with cards
on their local systems (i.e. without the need to connect to Blizzard's servers).

## Current utilities:
* Web scraper
* Deck-shuffling simulator
* Card searcher

### Web Scraper (complete)

Usage:
  
	python3 scraper.py 
	# Output: basic.txt, classic.txt, gvg.txt, 
	# naxx.txt, blackrock.txt, reward.txt, promo.txt

The web scraper pulls data from the 
[Hearthstone: Heroes of Warcraft Wiki](http://hearthstone.gamepedia.com/). It builds
seven(\*) lists of cards for each of the current card lists:

* Basic (132 collectable cards\*)
* Classic (245 collectable cards\*)
* Goblins vs Gnomes (123 collectable cards\*)
* Curse of Naxxramas (30 collectable cards\*)
* Blackrock Mountain (31 collectable cards\*)
* Reward (2 collectable cards\*)
* Promo (2 collectable cards\*)

Each of these lists is stored in a text file, which can then be accessed from the
other applications.

The scraper waits 10 seconds between requests to be somewhat courteous to the
Wiki's servers.

* \* Numbers are subject to change, based on additions/removals by Blizzard*

### Deck-shuffling Simulator (proof of concept)

The deck-shuffling simulator was originally just a quick script I wrote up after
getting annoyed by how often my opponents (Hunters) would get certain cards
('Kill Command'). Eventually, it might be used to properly shuffle a deck for
play simulation.

Usage:

	python3 deck_simulation.py
	# Output: None

### Card Searcher (mostly complete)

The card searcher allows you to search fo particular cards from a very particular
list: a list of cards you currently don't possess in your collection. At the
moment, this requires the user to manually create this list in a file named 
"missing.txt" (a sample file is provided). 

Usage:

	python3 hearth-util.py [--help or -h]
	# Output: None

## Future Utilities
* Full card list searcher (via card\_search.py)
* Deck builder
* Play simulator
