import re
import requests

page_link = "https://www.mongodb.com/try/download/shell"
regex = r"https:\/\/downloads\.mongodb\.com\/compass\/mongosh-\d\.\d\.\d-x64\.msi"

html_page = requests.get(page_link).text

matches = re.search(regex, html_page, re.MULTILINE)

mongo_link = matches.group()


def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)


download(mongo_link, "mongosh.msi")
