import logging
import os
from time import time
from pathlib import Path
from queue import Queue
from threading import threading

from download import get_links, download_link

logger = logging.getLogger(__name__)


class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            directory, link = self.queue.get()
            try:
                download_link(directory, link)
            finally:
                self.queue.task_done()

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
