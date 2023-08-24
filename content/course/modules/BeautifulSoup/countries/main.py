from bs4 import BeautifulSoup


with open("index.html", "r") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, "lxml")
    # pretty = soup.prettify() Seems clearly
    # tag = soup.find('h5') Find first element of item
    
    # tags = soup.find_all('h5') Find all elements of item
    # for tag in tags:
    #     print(tag.text) Just show text part of element
    
    # course_cards = soup.find_all('div', class_='card') Select element type and assign a variable for scrape items on the website
    # for course in course_cards:
    #     course_name = course.h5.text
    #     course_price = course.a.text.split()[-1] Looping on the selected element and scrape specified items
        
    #     print(f"{course_name} costs {course_price}") Parsing
       
    