import wikipedia
import search_google.api


def get_knowledge_wikipedia(term):
    #stuff
    # wikipedia.set_lang("sv")
    summary = wikipedia.summary(term, sentences=2)
    return summary

def get_knowledge_google(term):
    # Define buildargs for cse api
    s2ttest = 'cat'
    searchterm = ''
    searchterm = str(term)
    buildargs = {
    'serviceName': 'customsearch',
    'version': 'v1',
    'developerKey' : 'AIzaSyCyHJ_eKNSy6kSXvQafM3ExsKEf2Fuhe1M'
    }

    # Define cseargs for search
    cseargs = {
    'q': s2ttest, #searchterm
    'cx': '8144907c10b824ec2',
    'num': 1
    }
    results = search_google.api.results(buildargs, cseargs)
    results.preview()
    print("[INFO]: results:" + results)
    links = results.links
    print("[INFO]: links:" + links)
    return links
