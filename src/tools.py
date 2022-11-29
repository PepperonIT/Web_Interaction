"""
Tools module
Helper tools for the main funtions
"""

import config
import wikipedia
import search_google.api
import youtube_websearch as yt


def get_info_wikipedia(term, wiki_lang):
    """
    term: A string as input into a wikipedia search
    """
    wikipedia.set_lang(wiki_lang)
    summary = wikipedia.summary(term, sentences=2)
    try:
        page = wikipedia.page(term)
        wikiimage = page.images[0]
        print("[INFO]: wikiimage: " + wikiimage)# pylint: disable=superfluous-parens
        return summary, wikiimage

    except IndexError as error:
        print("no picture")
    
    return summary, "https://upload.wikimedia.org/wikipedia/commons/6/61/Wikipedia-logo-transparent.png"

def get_info_google(term):
    """
    Helper function that calls Google's API with custom CE and settings
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


def get_info_youtube(term):
    """
    Helper function that calls Youtubes API, fetching video url and time
    term: A string as input into a youtube websearch package
    """
    search_results = yt.video_search(term)
    # print(search_results)# pylint: disable=superfluous-parens
    links = search_results[0]["videoId"]
    print("[INFO]: youtube_link: " + links)# pylint: disable=superfluous-parens
    length = search_results[0]["lengthText"]
    split = length.split()
    print(split)
    """set duration depending on how long the video is (sec, min+sec or hours+min+sec)"""
    if len(split) == 2:
        dur = int(split[0])
    elif len(split) == 4:
        dur = int(split[0]) * 60 + int(split[2]) 
    elif len(split) == 6:
        dur = int(split[0]) * 360 + int(split[2]) * 60 + int(split[4])
        return
    else:
        dur = 15
    print(dur)
    return links, dur
    