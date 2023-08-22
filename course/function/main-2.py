travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, number_of_visit, city):
    new_country = {
        "country": country,
        "visits": number_of_visit,
        "cities": city
    }
    travel_log.append(new_country)

add_new_country("Turkey", 2000, ["Ankara", "Yozgard"])
print(travel_log)