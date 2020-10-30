import requests
from bs4 import BeautifulSoup


class onlineTranslator:

    def __init__(self, my_language, too_language, text):

        self.my_language = my_language
        self.too_language = too_language
        self.text = text

    def request(self):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        url = f"https://context.reverso.net/translation/{my_language}-{too_language}/{self.text}"
        response = requests.get(url, headers=user_agent)
        translator.bf4(response)

    def bf4(self, response):
        translate_list_word = list()
        translate_list_text = list()
        soup = BeautifulSoup(response.content, "html.parser")
        translete_word = soup.find_all('a', {'class': ['translation ltr dict adv', 'translation ltr dict first n',
                                                       'translation ltr dict no-pos']})
        translete_text = soup.find_all('span', {'class': 'text'})
        for text in translete_text:
            if len(text.text) > 30:
                my_str = text.text.replace('\n', '')
                my_str.strip()
                translate_list_text.append(my_str.strip())
        for text in translete_word:
            translate_list_word += text.text.split()

        translator.print_text(translate_list_word, translate_list_text)

    def print_text(self, word, text):
        print('200 OK', 'Translations', sep='\n')
        print('\nContext examples:\n')

        print(self.too_language.title(), 'Translations:')
        if len(word) > 5:
            for print_word in range(5):
                print(word[print_word])
        else:
            for print_word in word:
                print(print_word)
        print('\n' + self.too_language.title(), 'Examples:')
        if len(text) > 5:
            for print_text in range(5):
                print(f'{text[print_text]}:\n{text[print_text + 1]}\n')
        else:
            for print_text in range(len(text) - 1):
                print(f'{text[print_text]}:\n{text[print_text + 1]}\n')


if __name__ == '__main__':
    print("""Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish\n""")
    my_language = int(input('Type the number of your language:\n'))
    too_language = int(input('Type the number of language you want to translate to:\n'))
    world_lenguage = ('', 'arabic', 'german', 'english', 'spanish',
                      'french', 'hebrew', 'japanese', 'dutch', 'polish',
                      'portuguese', 'romanian', 'russian', 'turkish')
    my_language = world_lenguage[my_language]
    too_language = world_lenguage[too_language]
    text = input('Type the word you want to translate:\n')
    translator = onlineTranslator(my_language, too_language, text)
    translator.request()
