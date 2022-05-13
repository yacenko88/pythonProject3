import requests
from bs4 import BeautifulSoup

def req_g():

    response = requests.get('https://scrapingclub.com/exercise/list_basic/?page=1')
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='col-lg-4 col-md-6 mb-4')
    name = soup.find('h4', class_='card-title').text.replace('\n','')
    print(name)

def main():
    req_g()


if __name__=='__main__':
    main()