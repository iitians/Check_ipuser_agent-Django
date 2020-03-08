import requests

def get_location(ip):
    response = requests.get('http://ipinfo.io/' + ip).json()
    location = response.get('country', 'non available')
    return location