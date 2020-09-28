import requests


def pars_url(url):
    if 'https://' or 'http://' in url:
        r = requests.get(url)
    else:
        url = 'https://' + url
        r = requests.get(url)
    return r.text
