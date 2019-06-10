import requests
import dill
from bs4 import BeautifulSoup
from datetime import datetime


def get_link_date(el):
    url = 'https://web.archive.org'+ el.select('a')[0]['href']
    date = datetime.strptime(el.select('span')[-1].text, "%A, %B %d, %Y")#.strftime("%A, %B %d, %Y")
    return url, date

def get_links(response):
    soup = BeautifulSoup(response.text, "lxml")
    links = soup.select('div.views-row')
    return [get_link_date(link) for link in links]

def filter_by_date(links, cutoff=datetime(2014, 12, 1)):
    filtered_links = []
    for _ in range(len(links)):
        if links[_][1] <= cutoff:
            filtered_links.append(links[_])
    return filtered_links

def get_page_args(i):
    url = "https://web.archive.org/web/20150913224145/http://www.newyorksocialdiary.com/party-pictures"
    return {"url": url,
            "params": {"page": i}}

from requests_futures.sessions import FuturesSession

session = FuturesSession(max_workers=5)
link_list = [tech
         for future in [session.get(**get_page_args(i)) for i in range(26)]
         for tech in filter_by_date(get_links(future.result()))]
print(len(link_list))

dill.dump(link_list, open('nysd-links.pkd', 'wb'))
