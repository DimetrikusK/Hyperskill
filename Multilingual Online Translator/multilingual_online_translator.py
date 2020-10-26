import requests
from bs4 import BeautifulSoup


class onlineTranslator:

    def __init__(self, language, text):
        self.language = language
        self.text = text

    def request(self):
        print(self.text)
        if self.language == 'fr':
            url = f"https://context.reverso.net/translation/french-english/{self.text}"
        else:
            url = f"https://context.reverso.net/translation/english-french/{self.text}"
        print(url)
        reques = requests.get(url)
        print(reques)


    def bf4(self):
        pass


if __name__ == '__main__':
    language = input('Type "en" if you want to translate from French'
                ' into English, or "fr" if you want to translate'
                ' from English into French:\n')
    text = input('Type the word you want to translate:\n')
    print(f'You chose {language} as the language to translate "{text}" to.')
    translator = onlineTranslator(language, text)
    translator.request()
