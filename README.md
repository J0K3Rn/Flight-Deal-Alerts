# Flight-Deal-Alerts

A flight searching program which looks for low valued flights and sends a SMS alert. Default origin 
location is Airport IAH in Houston, TX

Features:
- Uses Sheety to read destination ideas and update IATA codes
- Uses Tequila to search for flights
- Search time frame is from tomorrow to 6 months
- Specify the maximum price wanted in the Google Sheets
- Sends out a SMS if a flight is below the maximum expected price
- Can easily switch to SMTP mail if SMS is deemed unworthy (See bottom of `notification_manager.py`)

How to run:
- Download repository
- Open downloaded repository with a command line interface
- Create an account on ![Twilio](https://www.twilio.com/), get your api key, account sid, phone numbers, 
and update `notification_manager.py`
- Create an account on ![Tequila](https://partners.kiwi.com/), get your api key and update `flight_search.py`
- Create an account on ![Sheety](https://sheety.co/), get your api key and update `data_manager.py`
- Create a Google Sheet and setup / give access to Sheety to access
- Fill out relevant info (See Excel screenshot below for example). There is no need to provide the IATA codes -> 
the program will do it for you
- Set a low price. The low prices I obtained were from Google flights
- run `pip install twilio`
- run `python main.py`
- Script will be run and message will be sent if flight price meets threshold. Can also easily be updated to send SMTP

Program Running Example:

![alt text](https://github.com/J0K3Rn/Flight-Deals-Alert/blob/main/screenshots/output.png?raw=true) 

Google Sheets Example:

![alt text](https://github.com/J0K3Rn/Flight-Deals-Alert/blob/main/screenshots/excel_sheet.png?raw=true) 

Google Flight Price Prediction:

![alt text](https://github.com/J0K3Rn/Flight-Deals-Alert/blob/main/screenshots/google_flights.png?raw=true) 
