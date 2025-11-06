from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



url=input('Enter Playlist URL:')
if not url.startswith('https://www.youtube.com/playlist?list='):
    print('Invalid URL. Please enter a valid YouTube playlist URL.')
    exit()
if requests.get(url).status_code==200:
    chromeconfig=webdriver.ChromeOptions()
    chromeconfig.add_experimental_option('detach', True)
    chromeconfig.add_argument('--headless')
    driver=webdriver.Chrome(chromeconfig)
    driver.get(url)
    time.sleep(1)
    body=driver.find_element(By.TAG_NAME, 'body')
    page_update= True
    last_len=0
    while page_update:
        for _scroll in range(5):
            body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        video_container=driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-playlist-video-list-renderer/div[3]')
        video_tags = video_container.find_elements(By.CLASS_NAME, 'yt-badge-shape__text')
        if len(video_tags) > last_len:
            last_len = len(video_tags)
        else:
            page_update = False
    i=1
    total_watch_time=0
    video_tags=video_container.find_elements(By.CLASS_NAME, 'yt-badge-shape__text')
    for video in video_tags:
        dur=video.text
        dur=dur.split(':')
        for i in range (-1,-len(dur)-1,-1):
            total_watch_time+=int(dur[i])*(60**(-i-1))
    days=total_watch_time//86400
    hours=(total_watch_time%86400)//3600
    minutes=(total_watch_time%3600)//60
    seconds=total_watch_time%60
    print(f'Total Playlist Watch Time:{int(days)} days {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds')
    driver.quit()

