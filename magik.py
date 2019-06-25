import csv
import requests
from bs4 import BeautifulSoup


def scrape(filename, url):
    html = load_html(url)
    result = get_data(html)
    write_csv = to_csv(filename, result)


def load_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    return response.text


def get_data(html):
    result = []
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='nav')
    span = div.find_all('span')
    current_nav = span[0].text
    result.append(current_nav)
    nav_change = span[-1].text
    result.append(nav_change)
    div = soup.find_all('div', class_='info-right-row')
    for each_div in div:
        result.append(each_div.span.text)
    return result


def to_csv(filename, result):
    fieldnames = ['nav', 'change', 'bid', 'offer', 'date']
    result = {k: v for k, v in zip(fieldnames, result)}
    with open(f'{filename}.csv', 'a+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(result)
