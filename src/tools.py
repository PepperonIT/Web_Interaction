"""
Tools module
Helper tools for the main funtions
"""

import wikipedia
import search_google.api
import config

def get_knowledge_wikipedia(term):
    """term"""
    wikipedia.set_lang("sv")
    summary = wikipedia.summary(term, sentences=1)
    return summary

def get_image_wikipedia(term):
    """term"""
    wikipedia.set_lang("sv")
    page = wikipedia.page(term)
    wikiimage = page.images[0]
    print("[INFO]: wikiimage: " + wikiimage)# pylint: disable=superfluous-parens
    return wikiimage

def get_image_google(term):
    """term"""
    # Define buildargs for api api
    buildargs = {
    "serviceName": "customsearch",
    "version": "v1",
    "developerKey": config.GOOGLE_API
    }
    # Define cseargs for search
    cseargs = {
    "q": term,
    "cx": config.GOOGLE_CX,
    "num": 1,
    "searchType": "image"
    }
    results = search_google.api.results(buildargs, cseargs)
    links = results.get_values('items', 'link')
    links = results.links
    links = str(links)
    links = links[3:-2]
    print("[INFO]: google_link: " + links)# pylint: disable=superfluous-parens
    return links