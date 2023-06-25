
# my_email = "1941012268.p.soumiksaha@gmail.com"
# my_password = "lypvmbdidhnjfrlx"

# with smtplib.SMTP("smpt.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="soumiksaha2000.ss@gmail.com", 
#         msg="Subject:Hello Soumik \n\n This is the body of my email."
#     )

import smtplib
import datetime as dt
import random


MY_EMAIL = "1941012268.p.soumiksaha@gmail.com"
MY_PASSWORD = "Buntyanshi"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("Day-32(Send Emails and SMTP)/Birthday Wisher (Day 32) start/quotes.txt", encoding="utf8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smpt.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject:Hello Soumik. Saturday's Motivation: \n\n {quote}.".encode("utf-8")
        )
