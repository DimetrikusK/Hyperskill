import requests
from bs4 import BeautifulSoup


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
    too_language = int(input("Type the number of a language you want"
                             " to translate to or '0' to translate to all languages:\n"))
    world_lenguage = [0, 'arabic', 'german', 'english', 'spanish',
                      'french', 'hebrew', 'japanese', 'dutch', 'polish',
                      'portuguese', 'romanian', 'russian', 'turkish']
    my_language = world_lenguage[my_language]
    too_language = world_lenguage[too_language]
    world_lenguage.remove(my_language)
    input_text = input('Type the word you want to translate:\n')
    if too_language == 0:
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
