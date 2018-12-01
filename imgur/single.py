import logging
import os
from time import time
from pathlib import Path

from download import get_links, download_link

logger = logging.getLogger(__name__)

def main():
    ts = time()
    # To set the environment variable in the terminal:
    # export IMGUR_CLIENT_ID='my-client-id'
    client_id = os.getenv('IMGUR_CLIENT_ID')

    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")

    if not os.path.isdir('images'):
        os.makedirs('images')

    links = get_links(client_id)
    for link in links:
        download_link(Path('images'), link)

    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()
