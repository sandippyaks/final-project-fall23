"""
Weather App to check the current weather based on zip code
"""
from city_weather import CityWeather
import requests
from pprint import pprint as pp
from weather_api_key import API_KEY as MY_API_KEY

#Set your API Key
API_KEY = MY_API_KEY  # TODO: Update with your API key
# Base URL for OpenWeatherMap
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

def pull_weather_data(zip_code, country='us'):
    api_url = BASE_URL + 'zip=' + str(zip_code)
    api_url += f',{country}' + '&units=metric'  # add country and units
    api_url += '&appid=' + API_KEY  # add your key
    try:
        # Connect to API and get data in JSON format
        weather_data = requests.get(api_url).json()
        if weather_data['cod'] != 200:  # response code
            raise ValueError
    except ValueError:
        print('Bad response from API')

    return weather_data


def find_hottest_city(weather_zips):
    # TODO: Find the hottest city
    pass


def find_coldest_city(weather_zips):
    # TODO: Find the coldest city
    pass


def main():
    """My main function driver
    """
    #TODO: Read zipcodes from file
    zip_file = 'zip_codes.txt'
    with open(zip_file, mode='r', encoding='utf-8')as zip_codes:
        for zip_code in zip_codes:
            print(f'Pulling data for zip code: [{zip_code.strip()}]')

            # TODO: Call pull_weather_data for each zip code
            
            # TODO: Store data in a CityWeather object
    # TODO: Compare the current temperature of all objects
    # TODO: print the hottest and coldest

    

if __name__ == '__main__':
    main()

    .