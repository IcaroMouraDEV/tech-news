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
    data = Selector(html_content).css('.next::attr(href)').get()

    if not data:
        return None

    return data


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    url = Selector(html_content).css(
        '.pk-share-buttons-wrap').attrib['data-share-url']
    title = Selector(html_content).css(
        '.entry-title::text'
    ).get().strip('\xa0')
    timestamp = Selector(html_content).css('.meta-date::text').get()
    writer = Selector(html_content).css('.n::text').get()
    reading_time = int(Selector(html_content).css(
        '.meta-reading-time::text').get().split(' ')[0])
    summary = Selector(html_content).css(
        '.entry-content p'
    ).xpath('string()').get()
    category = Selector(html_content).css('.label::text').get()

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'reading_time': reading_time,
        'summary': summary.strip(),
        'category': category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
