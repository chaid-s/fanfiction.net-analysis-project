#Fanfiction scraper

from fanfiction import Scraper

scraper = Scraper()

metadata = scraper.scrape_story_metadata(4041754)#4041754 is an id of a story

print(metadata)
