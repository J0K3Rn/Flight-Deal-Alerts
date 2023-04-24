from twilio.rest import Client
#import smtplib


TWILIO_ACCOUNT_SID = ""
TWILIO_API_KEY = ""
FROM_PHONE_NUMBER = ""
TO_PHONE_NUMBER = ""


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def send_message(self, flight):
        # Send out SMS message
        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                  f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to " \
                  f"{flight.return_date}"
        print(message)
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_API_KEY)
        update = client.messages.create(body=message, from=FROM_PHONE_NUMBER, to=TO_PHONE_NUMBER)

        # Send out an Email instead!
        # Comment out the commands above that send a SMS message
        # Uncomment the `import smtplib` at the top of this file
        # Un-Comment the commands below -
        # and update the information below for your account
        # my_email = ""
        # to_email = ""
        # password = ""
        # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=password)
        #     connection.sendmail(
        #         from_addr=my_email,
        #         to_addrs=to_email,
        #         msg=f"{header}\n\n{body}"
        #     )
