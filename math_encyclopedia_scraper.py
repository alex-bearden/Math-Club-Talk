#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Scrapes page names from Encyclopedia of Mathematics.

from helium import *

phrases_file = open('math_phrases.txt', 'w')

url = 'https://encyclopediaofmath.org/wiki/Special:AllPages'
start_chrome(url, headless=False)

counter = 1
total_count = 0
while True:
    page_results = find_all(S('div.mw-allpages-body > ul.mw-allpages-chunk > li > a'))
    for page in page_results:
        phrases_file.write(page.web_element.text + '\n')
    num_added = len(page_results)
    first_added = page_results[0].web_element.text
    last_added = page_results[-1].web_element.text
    total_count += num_added
    print(f' Page {counter} done\n',
          f'Phrases added: {num_added}\n',
          f'From: {first_added}\n',
          f'To: {last_added}\n',
          f'Total phrase count: {total_count}\n')
    counter += 1
    if Text('OK').exists():
        click('OK')
    if Text('Next page').exists():
        click('Next page')
    else:
        break
    
phrases_file.close()

kill_browser()