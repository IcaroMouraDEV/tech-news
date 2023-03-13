import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        html = requests.get({
            'url': url,
            'timeout': 3,
            'user-agent': 'Fake user-agent'
        })

        time.sleep(1)

        if html.status_code != 200:
            return None

        return html.text

    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    data = Selector(html_content).css('.cs-overlay-link::attr(href)').getall()

    return data


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
