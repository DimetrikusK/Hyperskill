import requests
from bs4 import BeautifulSoup, Comment


def request():
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f"https://context.reverso.net/translation/{'english'}-{'german'}/{'hello'}"
    response = requests.get(url, headers=user_agent)
    bf4(response)


def bf4(response):
    translate_list_word = []
    translate_list_text = []
    soup = BeautifulSoup(response.content, "html.parser")
    translete_word = soup.find_all('div', {'class': ['wide-container']})
    translete_text = soup.find_all('span', {'class': 'text'})
    # for text in translete_text:
    #     if len(text.text) > 30:
    #         my_str = text.text.replace('\n', '')
    #         translate_list_text.append(my_str.strip())
    tmp = []
    string = str

    #     my_str = text.text.replace('\n', '')
    #     translate_list_word += my_str.split()
    # print(translate_list_word)
    # # translate_list_word = translate_list_word[2].split()
    # text = []
    # for i in range(0, 1):
    #     print(translate_list_word)
    # for i in range(0, 2):
    #     text.append(translate_list_text)
    #     print(text)


request()

