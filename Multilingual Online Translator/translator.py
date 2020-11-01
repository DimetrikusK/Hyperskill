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
        response = session.get(url, headers=user_agent)
        return response

    def bf4(self, response):
        translate_list_word = []
        translate_list_text = []
        soup = BeautifulSoup(response.content, "html.parser")
        translete_word = soup.find_all('div', {'class': ['wide-container',
                                                         'translation ltr dict adv',
                                                         'translation ltr dict first n',
                                                         'translation ltr dict no-pos']})
        translete_text = soup.find_all('span', {'class': 'text'})
        for text in translete_text:
            if len(text.text) > 30:
                my_str = text.text.replace('\n', '')
                translate_list_text.append(my_str.strip())
        for text in translete_word:
            my_str = text.text.replace('\n', '')
            translate_list_word.append(my_str.strip())

        try:
            translate_list_word = translate_list_word[2].split()
        except:
            pass

        return translate_list_word, translate_list_text

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

    def save_to_file(self, word, text):
        with open(f'{self.text}.txt', 'a', encoding='UTF-8') as f:
            print(self.too_language.title(), 'Translations:')
            f.write(self.too_language.title() + ' ' + 'Translations:\n')
            try:
                print(word[0] + '\n')
                f.write(word[0] + '\n')
            except:
                pass
            print(self.too_language.title(), 'Examples:')
            f.write('\n' + self.too_language.title() + ' ' + 'Examples:\n')
            try:
                print(f'{text[1]}:\n{text[0]}\n')
                f.write(f'{text[1]}:\n{text[0]}\n\n')
            except:
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
    world_lenguage.remove(my_language)
    if too_language == 'all':
        for i in range(1, len(world_lenguage)):
            translator = onlineTranslator(my_language, world_lenguage[i], world_lenguage, input_text)
            response = translator.request()
            world, text = translator.bf4(response)
            translator.save_to_file(world, text)
    else:
        translator = onlineTranslator(my_language, too_language, world_lenguage, input_text)
        response = translator.request()
        world, text = translator.bf4(response)
        translator.print_text(world, text)
