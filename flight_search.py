import requests
import datetime
from dateutil.relativedelta import relativedelta
from flight_data import FlightData


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = ""
HEADER = {
    "apikey": f"{TEQUILA_API_KEY}"
}


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    # Get IATA code for each destination in the spreadsheet
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {
            "term": f"{city_name}",
            "location_types": "airport",
            "limit": "1",
            "active_only": "true"
        }
        response = requests.get(url=location_endpoint, headers=HEADER, params=query)
        location_data = response.json()["locations"]

        code = location_data[0]["id"]
        return code

    # Search for flights to destination anywhere from tomorrow to in 6 months
    def search_flight(self, origin, destination, airport, max_price):
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        in_six_months = (datetime.date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")
        query = {
            "fly_from": origin,
            "fly_to": airport,
            "date_from": tomorrow,
            "date_to": in_six_months,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "adults": 1,
            "curr": "USD",
            "max_stopovers": 2,
            "price_to": max_price,
            "vehicle_type": "aircraft",
        }
        response = requests.get(url=location_endpoint, headers=HEADER, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {airport}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=destination,
            destination_airport=airport,
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][-1]["local_departure"].split("T")[0]
        )
        # print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
