import requests
from bs4 import BeautifulSoup

def req_g():

    response = requests.get('https://scrapingclub.com/exercise/list_basic/?page=1')
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in data:
        name = i.find('h4', class_='card-title').text.replace('\n','')
        price = i.find('h5').text
        url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
        print(name + '\n' + price + '\n' + url_img + '\n\n')
    # print(data)

def main():
    req_g()


if __name__=='__main__':
    main()