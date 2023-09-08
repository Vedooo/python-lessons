from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class BiletallScraper:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.biletall_url = 'https://www.biletall.com'
        self.driver.maximize_window()

    def send_a_message():
        pass
    
    def pay_the_ticket():
        pass
    
    def select_seat():
        pass
    
    def select_ticket():
        pass
    
    def select_company(self, company):
        company_filter = self.driver.find_element(By.XPATH, value="//*[@id='quick-filters-container']/ul/li[6]/button")
        company_filter.click()
        
        option_active = True
        while option_active:
            company_dropdown = self.driver.find_element(By.XPATH, value="//*[@id='filters-bar']/ob-dropdown[1]")
            company_dropdown.click()
            company_elements = self.driver.find_elements(By.XPATH, value="//*[@id='filters-bar']/ob-dropdown[1]/div[2]/div/ul/li")
            company_list = [comp.text for comp in company_elements]    
            company_list = [comp.text for comp in company_elements]    

            company_list = [comp.text for comp in company_elements]

            if company not in company_list:
                print(f"{company} does not provide service on the route you have selected.")
                print("Available Options:")
                for i, comp in enumerate(company_list, start=1):
                    print(f"{i}. {comp}")
                
                try:
                    company_index = int(input("Choose an available company from the list (1-{}): ".format(len(company_list))))
                    if 1 <= company_index <= len(company_list):
                        selected_company = company_elements[company_index - 1]
                        company_name = selected_company.text
                        print(f"{company_name} selected.")
                        selected_company.click()
                        option_active = False
                    else:
                        print("Enter a valid number.")
                except ValueError:
                    print("Enter a valid number.")
            else:
                option_active = False
            
    def select_filters(self,date_period):
        if ',' in date_period:
            date_periods = date_period.split(',')
            for dp in date_periods:
                departure_filter = self.driver.find_element(By.XPATH, value="//*[@id='quick-filters-container']/ul")
                departure_filters = departure_filter.find_elements(By.XPATH, value='li')
                filter_list = [filter.text for filter in departure_filters]
                for filter in filter_list:
                    try:
                        if dp.strip() == filter:
                            index = filter_list.index(filter) + 1
                            xpath = f"//*[@id='quick-filters-container']/ul/li[{index}]/button"
                            filter_element = self.driver.find_element(By.XPATH, xpath)
                            filter_element.click()
                    except Exception as e:
                        print(e)

        else:
            departure_filter = self.driver.find_element(By.XPATH, value="//*[@id='quick-filters-container']/ul")
            departure_filters = departure_filter.find_elements(By.XPATH, value='li')
            filter_list = [filter.text for filter in departure_filters]
            for filter in filter_list:
                try:
                    if date_period == filter:
                        index = filter_list.index(filter) + 1
                        xpath = f"//*[@id='quick-filters-container']/ul/li[{index}]/button"
                        filter_element = self.driver.find_element(By.XPATH, xpath)
                        filter_element.click()
                except Exception as e:
                    print(e)
        
    def select_date(self, date):
        departure_input = self.driver.find_element(By.ID, value='departure-input')
        departure_input.click()
    
        buttons = self.driver.find_elements(By.CSS_SELECTOR, value="button[data-date]")
        time.sleep(2)
        for button in buttons:
            date_attribute = button.get_attribute("data-date")
            if date_attribute == date:
                button.click()
                break

    def search_tickets(self, origin, destination, date):
        self.driver.get(url=self.biletall_url)
        time.sleep(2)

        origin_input = self.driver.find_element(By.ID, 'origin-input')
        origin_input.click()
        origin_input.send_keys(origin)
        time.sleep(2)
        origin_input.send_keys(Keys.ENTER)
    
        destination_input = self.driver.find_element(By.ID, 'destination-input')
        destination_input.click()
        destination_input.send_keys(destination)
        time.sleep(2)
        destination_input.send_keys(Keys.ENTER)
        
        self.select_date(date)
        search_button = self.driver.find_element(By.XPATH, '//*[@id="search-button"]')
        search_button.send_keys(Keys.ENTER)
        time.sleep(5)
        
    def quit(self):
        self.driver.quit()


