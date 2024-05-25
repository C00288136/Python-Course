import smtplib

my_email = "soserer842002@gmail.com"
password = "michalsoserer"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() #secure connection
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="C00288136@setu.ie", msg="Hello")
connection.close()