from bs4 import BeautifulSoup
import requests


url=input('Enter Playlist URL:')
if not url.startswith('https://www.youtube.com/playlist?list='):
    print('Invalid URL. Please enter a valid YouTube playlist URL.')
    exit()
if requests.get(url).status_code==200:
    with open(url, 'r', encoding='utf-8') as file:
        soup=BeautifulSoup(file, 'html.parser')
