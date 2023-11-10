import requests
from datetime import datetime


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
    latitude_difference = iss_latitude - MY_LAT
    longitude_difference = iss_longitude - MY_LONG
    if 5 >= latitude_difference >= -5:
        return True
    elif 5 >= longitude_difference >= -5:
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



