import requests
from bs4 import BeautifulSoup
from time import sleep

def req_g():
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79 (Edition Yx GX)'}
    for count in range(1, 8):
        sleep(3)

        response = requests.get(f'https://scrapingclub.com/exercise/list_basic/?page={count}', headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for i in data:
            name = i.find('h4', class_='card-title').text.replace('\n','')
            price = i.find('h5').text
            url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
            print(name + '\n' + price + '\n' + url_img + '\n\n')


def main():
    req_g()


if __name__=='__main__':
    main()