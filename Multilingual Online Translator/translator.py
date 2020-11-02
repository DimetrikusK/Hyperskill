import requests
from bs4 import BeautifulSoup
import sys
import argparse


class onlineTranslator:

    def __init__(self, my_language, too_language, all_language, text):
        self.my_language = my_language
        self.too_language = too_language
        self.all_language = all_language
        self.text = text

    def request(self):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        session = requests.Session()
        url = f"https://context.reverso.net/translation/{self.my_language}-{self.too_language}/{self.text}"
        try:
            response = session.get(url, headers=user_agent)
            return response
        except requests.exceptions.RequestException:
            print('\nSomething wrong with your internet connection')
            return 0

    def bf4(self, response):
        translate_list_word = []
        translate_list_text = []
        tmp = []
        soup = BeautifulSoup(response.content, "html.parser")
        translete_word = soup.find_all('div', {'class': ['wide-container',
                                                         'translation ltr dict adv',
                                                         'translation ltr dict first n',
                                                         'translation ltr dict no-pos']})
        translete_text = soup.find_all('span', {'class': 'text'})
        for text_text in translete_text:
            if len(text_text.text) > 30:
                my_str = text_text.text.replace('\n', '')
                translate_list_text.append(my_str.strip())
        for text in translete_word:
            tmp.append(text.text.split('\n'))
        tmp = tmp[2]
        for text_word in tmp:
            if text_word != '':
                translate_list_word.append(text_word.strip())
        if len(translate_list_word) > 1:
            return translate_list_word, translate_list_text
        else:
            return 0


    def print_text(self, word, text):
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

    def save_to_file(self, word, text):
        with open(f'{self.text}.txt', 'a', encoding='UTF-8') as f:
            print(self.too_language.title(), 'Translations:')
            f.write(self.too_language.title() + ' ' + 'Translations:\n')
            try:
                print(word[0] + '\n')
                f.write(word[0] + '\n')
            except IndexError:
                pass
            print(self.too_language.title(), 'Examples:')
            f.write('\n' + self.too_language.title() + ' ' + 'Examples:\n')
            try:
                print(f'{text[1]}:\n{text[0]}\n')
                f.write(f'{text[1]}:\n{text[0]}\n\n')
            except IndexError:
                pass
            f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("my_language", default=str)
    parser.add_argument("too_language", type=str)
    parser.add_argument("input_text", type=str)
    name_key = parser.parse_args()
    my_language = name_key.my_language
    too_language = name_key.too_language
    input_text = name_key.input_text
    world_lenguage = [0, 'arabic', 'german', 'english', 'spanish',
                      'french', 'hebrew', 'japanese', 'dutch', 'polish',
                      'portuguese', 'romanian', 'russian', 'turkish']
    if too_language == 'all' or too_language in world_lenguage:
        world_lenguage.remove(my_language)
        if too_language == 'all':
            for i in range(1, len(world_lenguage)):
                translator = onlineTranslator(my_language, world_lenguage[i], world_lenguage, input_text)
                response = translator.request()
                if response != 0:
                    try:
                        world, text = translator.bf4(response)
                        translator.print_text(world, text)
                    except TypeError:
                        print(f'Sorry, unable to find {input_text}')
                        exit()
        else:
            translator = onlineTranslator(my_language, too_language, world_lenguage, input_text)
            response = translator.request()
            if response != 0:
                try:
                    world, text = translator.bf4(response)
                    translator.print_text(world, text)
                except TypeError:
                    print(f'Sorry, unable to find {input_text}')
    else:
        print(f"Sorry, the program doesn't support {too_language}")

