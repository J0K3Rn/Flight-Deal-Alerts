import requests
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

TOKEN = ""
SHEETY_LINK = ""
SHEETY_HEADER = {
    "Authorization": f"Bearer {TOKEN}"
}

ORIGIN_CITY_IATA = "IAH"

response = requests.get(SHEETY_LINK, headers=SHEETY_HEADER)
sheet_data = response.json()["prices"]

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
for trip in sheet_data:
    if trip["iataCode"] == '':
        trip["iataCode"] = flight_search.get_destination_code(trip["city"])
        data_manager.update_destination_code(row_id=trip['id'], code=trip['iataCode'])
    flight = flight_search.search_flight(origin=ORIGIN_CITY_IATA, airport=trip['iataCode'], destination=trip['city'],
                                         max_price=trip['lowestPrice'])
    if flight is not None:
        notification_manager.send_message(flight)
