

import requests
from bs4 import BeautifulSoup
from tkinter import *

from pyexpat.errors import messages

#
# target_url = input("Enter the website you wants us to show it's links")

foundLinks = []

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    return soup


def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0]
            if url in found_link and found_link not in foundLinks:
                foundLinks.append(found_link)
                urls.config(text= "\n".join(foundLinks))
                crawl(found_link)



def start_crawl():
    url = url_entry.get()
    crawl(url)

window = Tk()
window.title("Website Crawler")
window.minsize(width=600,height=600)



url_label = Label(text="Enter the website you want us to show it's links")
url_label.pack()

url_entry = Entry()
url_entry.pack()

url_button = Button(text="Enter",command=start_crawl)
url_button.pack()

urls = Label()
urls.pack()

window.mainloop()
