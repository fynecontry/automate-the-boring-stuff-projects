#!/usr/bin/env python3
# img_downloader.py     - searches flickr for CLI provided word and 
#                       downloads 10 images into a folder

import sys, os, logging, requests,bs4

logging.basicConfig(filename='img_downloader.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_keyword():
    # keyword obtained from CLI
    if len(sys.argv) < 2:
        print('usage: img_downloader.py [search_keyword]')
        sys.exit(1)
    else:
        search_keyword = ' '.join(sys.argv[1:])
    return search_keyword

def download_webpage(search_keyword):
    '''Search flickr using keyword and dowloads webpage'''
    url = 'https://www.flickr.com/search/?text=' + search_keyword
    # Download the page
    try:
        logging.info('Downloading page')
        res = requests.get(url)
        res.raise_for_status()
        logging.info('Downloaded page successfully')
    except Exception as err:
        print(f'There was a problem fetching page: {err}')
        logging.critical(f'Fetch {url} request failed: {err}')
        sys.exit(1)
    return res

def download_images(page_response):
    '''Retrive list of image elements from webpage reponse and save to disk'''
    page_soup = bs4.BeautifulSoup(page_response.text, 'html.parser')
    img_elems = page_soup.select('.photo-list-pjdkhoto-container')
    if img_elems == []:
        print('Could not find images')
        logging.warning('Empty img_elems list, page_soup could not find images using class: .photo-list-photo-container')


def main():
    # Get search word(s) from user
    search_keyword = get_keyword()

    #search and download result
    page_response = download_webpage(search_keyword)

    download_images(page_response)

if __name__ == "__main__":
    main()
