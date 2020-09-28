import requests
from requests.models import Response


def do_search(bookstore_url, params):
    r = requests.get(bookstore_url, params=params)
    return r


params = {'author': 'Austen', 'title': 'Emma'}
print(do_search('http://bookstore.com/search', params))
