#helpers.py

#imports
from googlesearch import search
from urlparse3 import urlparse3
from urllib.parse import urlparse

def retrieve_search_results(searchQuery, numResults=10):
    #results list
    results_list = list()
    #appending the results to results_list
    for result in search(searchQuery, num_results=numResults):
        results_list.append(result)
    #results dict contains the website name as key and the a['href'] as dict
    results_dict = dict()
    for result in results_list:
        t = urlparse(result).netloc
        t = ('.'.join(t.split('.')[1:]))
        # print(t)
        results_dict[t] = result
    # print(results_dict)
    return results_dict
