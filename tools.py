"""
Robot module
"""

import wikipedia

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
