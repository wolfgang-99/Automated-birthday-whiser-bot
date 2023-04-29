import pandas
import smtplib
import datetime as dt
import random

my_mail = "python1email1@gmail.com"
password = "Abcd1234()"


now = dt.datetime.now()
today_tuple = ( now.day, now.month)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data["day"]) : data_row for (index, data_row) in data.iterrows() }
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs=birthday_person["email"],
                            msg=f"subject: Happy Birthday\n\n {content}")