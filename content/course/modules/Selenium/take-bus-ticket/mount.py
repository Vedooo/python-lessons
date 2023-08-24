from datetime import datetime, timedelta

class DateRange:
    def __init__(self, start_date_str, end_date_str):
        self.start_date = datetime.strptime(start_date_str, "%y-%m-%d")
        self.end_date = datetime.strptime(end_date_str, "%y-%m-%d")
        self.date_range = self.generate_date_range()

    def generate_date_range(self):
        date_range = []
        current_date = self.start_date

        while current_date <= self.end_date:
            date_range.append(current_date.strftime("%y-%m-%d"))
            current_date += timedelta(days=1)

        return date_range