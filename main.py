import re
import requests
import hashlib

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


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
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)


page_link = "https://www.mongodb.com/try/download/shell"
mgdb_regex = r"https:\/\/downloads\.mongodb\.com\/compass\/mongosh-\d\.\d\.\d-x64\.msi"

html_page = requests.get(page_link).text
matches = re.search(mgdb_regex, html_page, re.MULTILINE)
mongo_link = matches.group()
file_name = mongo_link.split('/')[-1]

download(mongo_link, file_name)
print(get_hash(file_name))
