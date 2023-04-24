import requests


SHEETY_LINK = ""
SHEETY_PUT_LINK = ""
TOKEN = ""
SHEETY_HEADER = {
    "Authorization": f"Bearer {TOKEN}"
}


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def update_destination_code(self, row_id, code):
        trip_update_code = {
            "price": {
                "iataCode": code,
            }
        }
        requests.put(url=f"{SHEETY_PUT_LINK}{row_id}", headers=SHEETY_HEADER, json=trip_update_code)
