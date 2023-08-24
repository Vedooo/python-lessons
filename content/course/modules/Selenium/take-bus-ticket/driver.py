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

    def select_filters(self,date_period):
        if ',' in date_period:
            date_periods = date_period.split(',')
            for dp in date_periods:
                # Burada dp değişkeniyle işlem yapabilirsiniz
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

        # Tek bir değer gelmişse doğrudan işlem yap
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

        # departure_filter = self.driver.find_element(By.XPATH, value="//*[@id='quick-filters-container']/ul")
        # departure_filters = departure_filter.find_elements(By.XPATH, value='li')
        # filter_list = [filter.text for filter in departure_filters]
        # for filter in filter_list:
        #     try:
        #         if date_period == filter:
        #             index = filter_list.index(filter) + 1
        #             xpath = f"//*[@id='quick-filters-container']/ul/li[{index}]/button"
        #             filter_element = self.driver.find_element(By.XPATH, xpath)
        #             filter_element.click()
        #     except Exception as e:
        #         print(e)
        
        
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
