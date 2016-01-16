from geopy.geocoders import Nominatim
import pandas as pd


# geopy init
geolocator = Nominatim()


location = geolocator.geocode("Kohlberg (Esslingen)")
print(location.address)
