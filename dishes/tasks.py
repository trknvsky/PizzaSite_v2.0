from celery.task import task
import urllib.request
import requests
from bs4 import BeautifulSoup


@task()
def parsing_pizzas():
    url = 'http://127.0.0.1:8000/dishes/'
    response = requests.get(url)
    contents = response.text
    soup = BeautifulSoup(contents, 'lxml')

    pizzas_data = []
    dishes = soup.find_all('div', {'class': 'thumbnail'})

    for dish in dishes:
        pizza = {}
        images = dish.find_all('div', {'class': 'example3'})
        prices = dish.find_all('div', {'class': 'example_text'})
        names = dish.find_all('div', {'class': 'caption'})
        texts = dish.find_all('li')
        for image in images:
            pizza['image_url'] = image.img['src']
        for price in prices:
            pizza['price'] = price.h6.contents[0]
        for name in names:
            pizza['name'] = name.h3.contents[0]
        for text in texts:
            pizza['text'] = text.contents[0]
        if pizza not in pizzas_data:
            pizzas_data.append(pizza)

    print(pizzas_data)
