import requests
from datetime import datetime
import smtplib


def utc_to_cst(hr):
    local_hr = hr - 6
    return local_hr


MY_LAT = 32.543390  # Your latitude
MY_LONG = -94.784170  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LONG + 5 >= iss_longitude >= MY_LONG - 5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

sunrise = utc_to_cst(sunrise)
sunset = utc_to_cst(sunset)

time_now = datetime.now()


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def is_dark():
    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True
    else:
        return False


sender = "dwdeathwolf@gmail.com"
password = "nezinvlcxjckceys"
if is_dark() and is_close():
    with smtplib.SMTP(host="smtp.google.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs="jhecker2001@gmail.com",
            msg="Subject:ISS Overhead\n\nThe International Space Station is overhead! Look up!"
        )
