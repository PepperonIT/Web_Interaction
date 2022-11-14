"""
Tools module
Helper tools for the main funtions
"""

import config
import wikipedia
import search_google.api

def get_info_wikipedia(term):
    """
    term: A string as input into a wikipedia search
    """
    wikipedia.set_lang("sv")
    summary = wikipedia.summary(term, sentences=1)
    page = wikipedia.page(term)
    wikiimage = page.images[0]
    print("[INFO]: wikiimage: " + wikiimage)# pylint: disable=superfluous-parens

    return summary, wikiimage

def get_info_google(term):
    """
    term: A string as input into a google search engine
    """
    # Define buildargs for api api
    buildargs = {
        "serviceName": "customsearch",
        "version": "v1",
        "developerKey": config.GOOGLE_API
    }
    # Define cseargs for search
    cseargs = {
        "q": term + ";jpg/png",
        "cx": config.GOOGLE_CX,
        "num": 1,
        "searchType": "image"
    }
    results = search_google.api.results(buildargs, cseargs)
    links = results.get_values('items', 'link')
    links = results.links
    links = str(links[0])
    print("[INFO]: google_link: " + links)# pylint: disable=superfluous-parens
    return links
