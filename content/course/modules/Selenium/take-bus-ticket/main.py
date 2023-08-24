from mount import DateRange
from driver import BiletallScraper


if __name__ == "__main__":
    start_date_str = "23-01-01"
    end_date_str = "23-12-31"

    date_range = DateRange(start_date_str, end_date_str)

origin = input("Nereden: ").title()
destination = input("Nereye: ").title()
date = input("Tarihi girin (YYYY-MM-DD): ")
date_period = input("Günün hangi zamanı (Sabah, Öğlen, Akşam, Bağlayan Gece): ").title()

if origin and destination and date:
        try:
            driver = BiletallScraper()
            driver.search_tickets(origin, destination, date)
            driver.select_filters(date_period)
        finally:
            pass
    