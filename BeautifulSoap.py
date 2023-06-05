import requests
from bs4 import Beautifulsoup
url = "https://bank.gov.ua/"
try:
    r = requests.get(url)
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    soup = Beautifulsoup(r.text, 'lxml')

    print(soup.find_all('title'))
    print(soup.find_all('p'))
    print(len(soup.find_all('p')))

    page_p = soup.find('p')
    text = page_p.get_text()
    print(text)

   page_h4 = soup.find('h4')
    text1 = page_h4.get_text()
    print(text1)
    print(len(text1))

    page_a = soup.find('a')
    text2 = page_a.get_text()
    print(text2)

    href = page_a.get('href')
    print(href)

    page = soup.find_all('li')
    urls = []
    for tag in page:
        tag = tag.find('a')
        if tag:
            href = tag.get('href')
            urls.append(href)
    print(urls)


    a_tag = soup.find_all('a')
    for i in range(10):
        print(a_tag[i])


