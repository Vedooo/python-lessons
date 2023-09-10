from mount import DateRange
from driver import BiletallScraper


inputs = {
    "from": "From: ",
    "to": "To: ",
    "date": "Choose Date(YYYY-MM-DD): ",
    "date_period": "Which period of the day(Sabah, Öğlen, Akşam, Bağlayan Gece), also type for (2+1) seat: ",
    "company": "Choose company: "
}

if __name__ == "__main__":
    start_date_str = "23-01-01"
    end_date_str = "23-12-31"

    date_range = DateRange(start_date_str, end_date_str)

origin = input(inputs["from"]).title()
destination = input(inputs["to"]).title()
date = input(inputs["date"])
date_period = input(inputs["date_period"]).title
company = input (inputs["company"]).title()

if origin and destination and date:
    try:
        driver = BiletallScraper()
        driver.search_tickets(origin, destination, date)
        driver.select_filters(date_period)
        driver.select_company(company)
    finally:
        driver.quit()
    