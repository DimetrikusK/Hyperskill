import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str)
key = parser.parse_args()
os.makedirs(key.dir, exist_ok=True)

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


def write_file(text, site):
    site_dir = '/' + site
    with open(key.dir + site_dir, 'w') as f:
        f.write(text)
    add_site_stak(site)


def check_site(command):
    site = command[0:command.find('.')]
    if "bloomberg" in site:
        print(bloomberg_com)
        write_file(bloomberg_com, site)
    elif "nytimes" in site:
        print(nytimes_com)
        write_file(nytimes_com, site)

def add_site_stak(site):
    global stak
    stak = [site]


def print_site_stak():
    if len(stak) > 0:
        print(stak.pop())





def main():
    while True:
        command = input()
        if '.com' in command:
            check_site(command)
        elif command is 'back':
            print_site_stak()
        elif command == 'exit':
            exit()
        else:
            print('Error: Incorrect URL')


main()
