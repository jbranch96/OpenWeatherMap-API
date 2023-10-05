#!/usr/bin/env python # [1]
"""
This script calls the OpenWeatherMap API and will display weather data in the terminal from the API response.
The user will be able to interact with the application via the terminal in order to specify the Zip Code and Country Code to use
during an API request. [2]

Usage: console_app.py
"""

# standard library imports, [3]
import requests # import the request module in order to make the API request
from configparser import ConfigParser # import ConfigParser in order to read API key from .cfg file
from datetime import datetime # import datetime for formatting and displaying sunrise/sunset time 

base_url = 'https://api.openweathermap.org/data/2.5/weather?zip='
FILE_PATH = './Weather Map App Settings.cfg'

def get_info_from_user():
     # Use this function to get the zip code, country code, and unit type from the user
    while True:
        # Todo - Add verification for the zip code entry
        zip_code = input('Enter a valid zip code: ')
        if zip_code != '':
            break
        else:
            continue

    while True:
        # Todo - Add verification for the country code entry
        country_code = input('Enter a valid country code (e.g. us): ')
        if country_code != '':
            break
        else:
            continue

    while True:
        # Todo - Add verification for the unit type entry
        unit_type_enum = input('Enter a number to represent the desired unit type for the temperature, [0 - Standard, 1 - Metric, 2 - Imperial]: ')
        if unit_type_enum == '0':
            unit_type = 'standard'
            break
        if unit_type_enum == '1':
            unit_type = 'metric'
            break
        if unit_type_enum == '2':
            unit_type = 'imperial'
            break
        else:
            continue

    return {'Zip Code' : zip_code , 'Country Code' : country_code , 'Unit Type' : unit_type}


def read_API_key_from_file(file_path):
    # Use this function to read in the API key from the .config file
    # instantiate
    config = ConfigParser()

    # parse existing file
    config.read(file_path)

    # read values from a section
    API_key_string = config.get('API Key', 'Value')

    return API_key_string


def form_full_url(api_key , base_url , user_info_dict):
    # full URL = base URL + zip code + ',' + country code + '&appid=' + API key + '&units=' + unit type
    full_url = base_url + user_info_dict['Zip Code'] + ',' +  user_info_dict['Country Code'] + '&appid=' + api_key 
    full_url = full_url + '&units=' + user_info_dict['Unit Type']

    return full_url


def print_weather_data(weather_data , user_info_dict):
    hpa_to_mmHg_conversion_factor = 33.86389
    pressure_mmHg = str(round(float(weather_data['main']['pressure'])/hpa_to_mmHg_conversion_factor,2))
    utc_sunrise_time = (weather_data['sys']['sunrise'] + weather_data['timezone'])
    utc_sunset_time = (weather_data['sys']['sunset'] + weather_data['timezone'])
    temperature_unit = ''
    
    if user_info_dict['Unit Type'] == 'standard': # (Kelvin)
        temperature_unit = '(Kelvin)'
    if user_info_dict['Unit Type'] == 'metric': # (Celsius)
        temperature_unit = '(deg C)'
    if user_info_dict['Unit Type'] == 'imperial': # (Farenheit)
        temperature_unit = '(deg F)'

    print(F"\nLocation (City, Country): {weather_data['name']}, {weather_data['sys']['country']}")
    print(F"Geo coordinates (Lon, Lat): {weather_data['coord']['lon']}, {weather_data['coord']['lat']}")
    print(F"Current temperature {temperature_unit}: {weather_data['main']['temp']}")
    print(F"Feels like {temperature_unit}: {weather_data['main']['feels_like']}")
    print(F"Humidity (%): {weather_data['main']['humidity']}")
    print(F"Max temperature {temperature_unit}: {weather_data['main']['temp_max']}")
    print(F"Min temperature {temperature_unit}: {weather_data['main']['temp_min']}")
    print(F"Air Pressure (mm Hg): {pressure_mmHg}")
    print(F"Weather description: {weather_data['weather'][0]['description']}")
    print(F"Weather condition: {weather_data['weather'][0]['main']}")
    print("Sunrise:", datetime.utcfromtimestamp(utc_sunrise_time).strftime('%Y-%m-%d %I:%M:%S'), 'AM')
    print("Sunset:" , datetime.utcfromtimestamp(utc_sunset_time).strftime('%Y-%m-%d %I:%M:%S'), 'PM\n')


def start_screen():
    print('\nWelcome to the OpenWeatherMap API Example script!')
    print('With this utlity you will be able to get current weather information based on zip code and country code.')
    print('Press enter to continue')
    input()

def main():
    start_screen() # display start-up text in the console

    api_key = read_API_key_from_file(FILE_PATH) # read the API key from the .cfg file
    
    if api_key == '':
        print('Failed to read API key from the Weather Map App Settings.cfg file, application will now terminate.')

    else:
        while True:
            user_info_dict = get_info_from_user() # get zip code, country code, and unit type desired from user
            full_url = form_full_url(api_key , base_url , user_info_dict) # build the full URL for the API call

            try:
                print('\nFetching data from OpenWeatherMap API...')

                response = requests.get(full_url) # opening a network connection and fetching data
                if response.status_code == 200: # status code, success:200
                    weather_data  = response.json()
                    print_weather_data(weather_data , user_info_dict)
                    user_input = input('Would you like to run this application again? Yes - [Y] , No - [Any other key]: ')

                    if user_input == 'Y' or user_input == 'y':
                        print() # skip line and re-run application
                        continue
                    else:
                        break
                
                else:
                    print('API request failed to return successfully.')
                    print('API response status code: ' , response.status_code)
                    print('API request failed to return successfully from the requested URL: ' , full_url)
                    break

            except:
                print('\nCould not access the requested URL.')
                print('Failed to reach: ' , full_url)
                break


# run the main application by calling main ()
if __name__ == '__main__': 
    main()
    