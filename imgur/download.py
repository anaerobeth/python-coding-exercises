"""
A script that downloads images from the web
Based on https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python
"""

import json
import logging
import os
from urllib.request import urlopen, Request
import pdb

logger = logging.getLogger(__name__)

URL = 'https://api.imgur.com/3/gallery/random/random/'
types = {'image/jpeg', 'image/png'}

def get_links(client_id):
    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    req = Request(URL, headers=headers, method='GET')
    try:
        resp = urlopen(req)
        data = json.loads(resp.read().decode('utf-8'))
        return [item['link'] for item in data['data'] if 'type' in item and item['type'] in types]
    except:
        print('Error retrieving images')


def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    image = urlopen(link)
    with download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)
