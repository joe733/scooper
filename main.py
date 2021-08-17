import re
import hashlib
import requests as rq
from tqdm import tqdm
from urllib import request


BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def get_hash(path):
    sha_256 = hashlib.sha256()

    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha_256.update(data)

    return sha_256.hexdigest()


def download(url, file_name):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        request.urlretrieve(
            url, filename=file_name, reporthook=t.update_to)


page_link = "https://www.mongodb.com/try/download/shell"
mgdb_regex = r"https:\/\/downloads\.mongodb\.com\/compass\/mongosh-\d\.\d\.\d-x64\.msi"

html_page = rq.get(page_link).text
matches = re.search(mgdb_regex, html_page, re.MULTILINE)
mongo_link = matches.group()
file_name = mongo_link.split('/')[-1]

download(mongo_link, file_name)
print(get_hash(file_name))
