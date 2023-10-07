import requests
import re
from lxml import html
import json
import csv
import click

# def get_digit(x):
#     if x.isdigit():
#         return x

def write_to_json(filename, data):
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()

def write_to_csv(filename, data):
    headers = ['title', 'price', 'in_stock', 'description']
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerow(data)

@click.command()
@click.option('--bookurl',
              help='Please provide a book url from books.toscrape.com' 
              ,default = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
@click.option('--filename',
              help='Please provide a filename CSV/JSON' 
              ,default = 'output.json')
def scrape(bookurl, filename):
    #url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

    response = requests.get(bookurl)
    tree = html.fromstring(html=response.text)

    content_inner = tree.xpath('//*[@id="content_inner"]/article')[0]
    title = content_inner.xpath('.//div[1]/div[2]/h1/text()')[0]
    price = content_inner.xpath('.//div[1]/div[2]/p[1]/text()')[0]
    availability = content_inner.xpath('.//div[1]/div[2]/p[2]/text()')[1].strip()
    in_stock = ''.join(list(filter(lambda x:x.isdigit(), availability)))  

    # or re.compile(r'\d+').findall(availability) with regex module
    # or use function for digit check and parse digit

    description = tree.xpath('//*[@id="content_inner"]/article/p/text()')[0]
    book_information = {
        'title': title,
        'price': price,
        'in_stock': in_stock,
        'description': description,
    }

    print(book_information)
    extension = filename.split('.')[1]
    if extension == 'json':
        write_to_json(filename,book_information)
    elif extension == 'csv':
        write_to_csv(filename,book_information)
    else:
        click.echo('The extension you provided is not supported, please use csv or json')
        
        
if __name__ == '__main__':
    scrape()