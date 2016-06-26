from YourLocation import get_your_coordinates
from GoogleMapAPIKey import get_google_coordinates
import json
import requests
from GetRequestAPI import uber_get_price

def main():
    # if you want this to grab current location run get_coordinates() and pass as location
    # your_coordinates = get_your_coordinates()
    detroit_lat = 42.33142699999999
    detroit_lng = -83.0457538
    detroit_address = '{latitude},{longitude}'.format(latitude=detroit_lat, longitude=detroit_lng)

    google_stores = get_google_coordinates(detroit_address, "Meijer")
    dump = google_stores['results'][0]['geometry']['location']
    # returns "geometry": {"location": {"lng": -83.11925870000002, "lat": 42.4443254}}

    end_loc_lat = dump['lat']
    end_loc_lon = dump['lng']

    output = uber_get_price(detroit_lat, detroit_lng, end_loc_lat, end_loc_lon)

    with open('output.JSON', 'w') as outfile:
        json.dump(output, outfile)

if __name__ =='__main__':
    main()