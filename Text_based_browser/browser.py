# coding: utf-8
import os
import argparse
import requests
# from .parsing import pars_site
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Back, Style
colorama.init()

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str)
key = parser.parse_args()
os.makedirs(key.dir, exist_ok=True)


def btf_soup(url, file_name):
    global stak
    reques = requests.get(url)
    soup = BeautifulSoup(reques.content, "html.parser")
    src = ('[document]', 'head', 'script', 'style',
           'body', 'html', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'title', 'table', 'div', 'li', 'form')
    tmp = soup.find_all(src)
    file = open(key.dir + '/' + file_name, 'w', encoding='utf-8')
    for i in tmp:
        print(Fore.MAGENTA, i.text)
        print(i.text, file=file)
    file.close()

    if flag != 0:
        with open(key.dir + '/' + file_name, 'r', encoding='utf-8') as file:
            stak.append(file.read())
            return None
    else:
        return None


def validation_url(url):
    if 'http' not in url:
        url = 'https://' + url
    return url


def name_file(url):
    if 'https' in url:
        file_name = url[8:]
    else:
        file_name = url[6:]
    i = file_name.find('/')
    file_name = file_name[0:i]
    btf_soup(url, file_name)


def print_site_stak():
    if len(stak) > 1:
        print(stak.pop())
    elif len(stak) == 0:
        pass
    else:
        print(Fore.CYAN, stak[0][0])
    browser()


def browser():
    global flag
    while True:
        command = input()
        if '.' in command:
            name_file(validation_url(command))
            if flag == 0:
                flag += 1
        elif "back" in command:
            print_site_stak()
        elif command == 'exit':
            exit()
        else:
            print(Fore.RED, 'Error: Incorrect URL')


flag = 0
stak = []
browser()
