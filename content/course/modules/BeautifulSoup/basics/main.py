from bs4 import BeautifulSoup
import requests

url = 'https://news.ycombinator.com'

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
title = soup.title.text
a_tag_list = soup.find_all('span', class_='titleline')
article_texts = []
article_links = []
for a_tag in a_tag_list:
    a_text = a_tag.getText()
    article_texts.append(a_text)
    a_link = a_tag.select_one('span a')['href']
    article_links.append(a_link)
    
a_score_list = [int(score.getText().split()[0]) for score in soup.find_all('span', class_='score')]

largest_number = max(a_score_list)
largest_index = a_score_list.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])


# print(article_texts)
# print(article_links)
# print(a_score_list)


##basics

# with open("website.html", encoding='utf-8') as html_file:
#     content = html_file.read()
    
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.a)
# all_a_tags = soup.find_all(name='a')

# for tag in all_a_tags:
    # print(tag.getText())
    # print(tag.get('href'))
    # pass

# heading = soup.find('h1', id='name') #Find first element
# print(heading)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.text)
# print(section_heading.name)
# print(section_heading.get('class'))

# p = soup.p.em.strong.a.get('href')
# p_another = soup.select_one(selector='p a')
# name_selector = soup.select_one(selector='#name')
# print(p)
# print(p_another)
# print(name_selector)

# heading = soup.select(".heading")
# print(heading)