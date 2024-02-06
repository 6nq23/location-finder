import phonenumbers
from phonenumbers import geocoder,timezone,carrier

# phone = input("Enter the phone number: ")
phone = "+919924863749"
ch_nmber = phonenumbers.parse(phone, "ch")
country = geocoder.description_for_number(ch_nmber, "en")
time_zone = timezone.time_zones_for_number(ch_nmber)
carr = carrier.name_for_number(ch_nmber, "en")
print(country,time_zone,carr)