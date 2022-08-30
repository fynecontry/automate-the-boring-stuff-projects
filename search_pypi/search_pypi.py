#!/usr/bin/env python3
# search_pypi.py     - Opens several search results

import sys, requests, webbrowser, bs4, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

print('Searching...')   # display text while downloading search results page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

logging.info('search results downloaded successfully')

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
link_elems = soup.select('.package-snippet')
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)

logging.info('operations successful')
