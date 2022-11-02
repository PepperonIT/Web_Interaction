import wikipedia


def get_knowledge_wikipedia(term):
    #stuff
    # wikipedia.set_lang("sv")
    # wikipedia.set_lang("en")
    summary = wikipedia.summary(term, sentences=2)
    return summary

def get_image_wikipedia(term):
    page = wikipedia.page(term)
    wikiimage = page.images[0]
    print("[INFO]: wikiimage: " + wikiimage)
    return wikiimage


# def get_knowledge_google(term):
    # Define buildargs for cse api

