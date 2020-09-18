import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str)
key = parser.parse_args()

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow
and change shape, and that could be a boon to medicine
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's
 Bad Moon Rising. The world is a very different place than
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


class Browser(bloomberg_com, nytimes_com):

    def __init__(self, site, key):
        self.text = str
        self.site = site
        self.key = key
        self.file_name = self.key + '/' + self.site

    def chek_site(self):
        self.site = self.site[0:self.site.find('.')]
        if self.site in "bloomberg.com":
            self.text = bloomberg_com
        elif self.site in "nytimes.com":
            self.text = nytimes_com

    def ft_print(self):
        with open(self.file_name, 'w') as f:
            f.write(self.text)
            f.close()

    def __str__(self):
        print(self.text)


def main(key):
    os.makedirs(key, exist_ok=True)
    while True:
        site = input()
        if '.' in site:
            Browser(site, key)
        elif site == 'exit':
            exit()
        else:
            print('Error: Incorrect URL')


main(key.dir)