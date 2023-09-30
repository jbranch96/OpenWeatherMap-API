#!/usr/bin/env python # [1]
"""
This script calls the OpenWeatherMap API and will display weather data in the terminal from the API response.
The user will be able to interact with the application via the terminal in order to specify the Zip Code and Country Code to use
during an API request. [2]

Usage: app.py
"""

# standard library imports, [3]
import requests # importing the request module
from configparser import ConfigParser # importing ConfigParser in order to read API key from .cfg file

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
        country_code = input('Enter a valid country code: ')
        if country_code != '':
            break
        else:
            continue

    while True:
        # Todo - Add verification for the unit type entry
        unit_type_enum = input('Enter a number to represent the desired unit type, [0 - Standard, 1 - Metric, 2 - Imperial]: ')
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
("This is the first line of my text, "
"which will be joined to a second.")

def form_full_url(api_key , base_url , user_info_dict):
    # full URL = base URL + zip code + ',' + country code + '&appid=' + API key + '&units=' + unit type
    full_url = base_url + user_info_dict['Zip Code'] + ',' +  user_info_dict['Country Code'] + '&appid=' + api_key 
    full_url = full_url + '&units=' + user_info_dict['Unit Type']

    return full_url

def main():

    api_key = read_API_key_from_file(FILE_PATH)
    if api_key == '':
        print('Failed to read API key from the Weather Map App Settings.cfg file, application will now terminate.')
    else:
        user_info_dict = get_info_from_user()
        full_url = form_full_url(api_key , base_url , user_info_dict)

        try:
            print('Fetching data from OpenWeatherMap API...\n')
            response = requests.get(full_url) # opening a network connection and fetching data
            if response.status_code == 200: # status code, success:200
                api_result = response.json()
                print('API result data: \n\n' , api_result, end='\n\n')
            else:
                print('\nAPI request failed to return successfully.')
                print('API response status code: ' , response.status_code)
                print('API request failed to return successfully from the requested URL: ' , full_url)
        except:
                print('\nCould not access the requested URL.')
                print('Failed to reach: ' , full_url)


# run the main application by calling main ()
if __name__ == '__main__': 
    main()