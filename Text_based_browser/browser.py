# coding: utf-8
import os
import argparse
from


parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str)
key = parser.parse_args()
os.makedirs(key.dir)


def write_file(text, site):
    site_dir = '/' + site
    with open(key.dir + site_dir, 'w') as f:
        f.write(text)
    browser()


def add_site_stak(text):
    stak.append(text)
    browser()


def print_site_stak():
    if len(stak) > 1:
        print(stak.pop())
    elif len(stak) == 0:
        pass
    else:
        print(stak[0])
    browser()


def browser():
    global flag
    while True:
        command = input()
        if '.' in command:
            text = pars_url(command)
            if flag == 0:
                flag += 1
            else:
                add_site_stak(text)
        elif "back" in command:
            print_site_stak()
        elif command == 'exit':
            exit()
        else:
            print('Error: Incorrect URL')


flag = 0
stak = []
browser()
