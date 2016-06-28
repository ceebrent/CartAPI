import requests

def uber_get_price(start_lat, start_long, end_lat, end_long):

    url = 'https://api.uber.com/v1/estimates/price'

    parameters = {
        'server_token': 'UBER_API_KEY',
        'start_latitude': start_lat,
        'start_longitude': start_long,
        'end_latitude': end_lat,
        'end_longitude':end_long,
        'seat_count':1
    }

    response = requests.get(url, params=parameters)

    data = response.json()
    return data

