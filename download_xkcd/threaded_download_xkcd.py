#!/usr/bin/env python3
#threaded_download_xkcd.py  -   Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading, logging

logging.basicConfig(filename='threaded_download_xkcd.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page.
        logging.info(f'Fetching page https://xkcd.com/{url_number}')
        print(f'Downloading page https://xkcd.com/{url_number}...')
        res = requests.get(f'https://xkcd.com/{url_number}')
        res.raise_for_status()
        logging.info(f'Fetched https://xkcd.com/{url_number} successfully')

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            logging.warning('Empty comic_elem list')
            print('Could not find the image.')
        else:
            comic_url = comic_elem[0].get('src')
            # Download the image.
            logging.info(f'Fetching image {comic_url}')
            print(f'Downloading image {comic_url}...')
            res = requests.get('https:' + comic_url)
            res.raise_for_status()
            logging.info('Fetched image {url_number} successfully')

            # Save the image to ./xkcd.
            logging.info('Writing image to disk')
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()
            logging.info('Write successful')

# Create and start the Thread objects
download_threads = []           # a list of all the Thread objects
for i in range(0, 140, 10):     # loops 14 times, create 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1       # There is no comic 0, so set it to 1.
    
    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()


# Wait for all Threads to end.
for i, download_thread in enumerate(download_threads):
    download_thread.join()
print('Done.')





        
