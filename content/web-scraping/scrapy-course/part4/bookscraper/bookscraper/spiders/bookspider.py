import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()
            
            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
            yield response.follow(book_url, callback=self.parse_book_page)
        
        next_page = response.css('h3 a ::attr(href)').get()
        
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback=self.parse_book_page)
            
    
    def parse_book_page(self, response):
        table_rows = response.css('table tr')
        yield {
            'url': response.url,
            'title': response.xpath('//*[@id="default"]/div/div/ul/li[4]/text()').get(),
            'product_type': table_rows[1].css('tr td::text').get(),
            'price_excl_tax': table_rows[2].css('tr td::text').get(),
            'price_incl_tax': table_rows[3].css('tr td::text').get(),
            'tax': table_rows[4].css('tr td::text').get(),
            'availability': table_rows[5].css('tr td::text').get(),
            'number_of_reviewers': table_rows[6].css('tr td::text').get(),
            'stars': response.css("p.star-rating").attrib['class'],
            'category': response.xpath('//*[@id="default"]/div/div/ul/li[3]/a/text()').get(),
            'description':  response.xpath('//*[@id="content_inner"]/article/p/text()').get(),
            'price': response.css('p.price_color::text').get()
        }