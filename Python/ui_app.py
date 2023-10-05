#!/usr/bin/env python # [1]
"""
This script calls the OpenWeatherMap API and will display weather data in the UI from the API response.
The user will be able to interact with the application via the UI entries and buttons in order to specify
the Zip Code and Country Code to use during an API request. [2]

Usage: ui_app.py
"""
# standard library imports, [3]
import requests # import the request module in order to make the API request
from configparser import ConfigParser # import ConfigParser in order to read API key from .cfg file
from datetime import datetime # import datetime for formatting and displaying sunrise/sunset time 
import tkinter as tk # import tkinter module for creating GUI

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?zip='
FILE_PATH = './Weather Map App Settings.cfg'

class MainApplication(tk.Frame):
        
    def __init__(self, master, BASE_URL, file_path):
        self.master = master
        self.base_url = BASE_URL
        self.file_path = file_path
        tk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()
   
    def configure_gui(self):
        root.title('OpenWeathermMap Example - Current Weather GUI') # give root window a title
        root.geometry('750x400') # specify root window dimensions
        root['bg'] = 'teal'

    def create_widgets(self):
        ### Weather data read-only entries on right-hand side of GUI ###
        self.loc_entry_lbl = tk.Label(root , text= 'Location (City, Country)')
        self.loc_entry_lbl.place(relx = 0.485, rely = 0.05, anchor = 'ne')
        self.loc_entry = tk.Entry(root, width= 25, state='readonly')
        self.loc_entry.place(relx = 0.5, rely = 0.1, anchor = 'ne')

        self.temp_lbl = tk.Label(root , text= 'Temperature')
        self.temp_lbl.place(relx = 0.7, rely = 0.05, anchor = 'ne')
        self.temp_entry = tk.Entry(root, width= 25, state='readonly')
        self.temp_entry.place(relx = 0.75, rely = 0.1, anchor = 'ne')

        self.vis_lbl = tk.Label(root , text= 'Visibility (m)')
        self.vis_lbl.place(relx = 0.95, rely = 0.05, anchor = 'ne')
        self.vis_entry = tk.Entry(root, width= 25, state='readonly')
        self.vis_entry.place(relx = 1, rely = 0.1, anchor = 'ne')
        ###__________________________row 1 end_________________________________###
        self.geocoord_entry_lbl = tk.Label(root , text= 'Geo Coordinates (Lon, Lat)')
        self.geocoord_entry_lbl.place(relx = 0.495, rely = 0.15, anchor = 'ne')
        self.geocoord_entry = tk.Entry(root, width= 25, state='readonly')
        self.geocoord_entry.place(relx = 0.5, rely = 0.2, anchor = 'ne')

        self.feels_like_lbl = tk.Label(root , text= 'Feels Like')
        self.feels_like_lbl.place(relx = 0.685, rely = 0.15, anchor = 'ne')
        self.feels_like_entry = tk.Entry(root, width= 25, state='readonly')
        self.feels_like_entry.place(relx = 0.75, rely = 0.2, anchor = 'ne')
       
        self.windspeed_lbl = tk.Label(root , text= 'Wind Speed (mph)')
        self.windspeed_lbl.place(relx = 0.975, rely = 0.15, anchor = 'ne')
        self.windspeed_entry = tk.Entry(root, width= 25, state='readonly')
        self.windspeed_entry.place(relx = 1, rely = 0.2, anchor = 'ne')
        ###__________________________row 2 end_________________________________###
        self.desc_entry_lbl = tk.Label(root , text= 'Weather Discription')
        self.desc_entry_lbl.place(relx = 0.47, rely = 0.25, anchor = 'ne')
        self.desc_entry = tk.Entry(root, width= 25, state='readonly')
        self.desc_entry.place(relx = 0.5, rely = 0.3, anchor = 'ne')

        self.min_temp_lbl = tk.Label(root , text= 'Min Temperature')
        self.min_temp_lbl.place(relx = 0.715, rely = 0.25, anchor = 'ne')
        self.min_temp_entry = tk.Entry(root, width= 25, state='readonly')
        self.min_temp_entry.place(relx = 0.75, rely = 0.3, anchor = 'ne')

        self.wind_dir_lbl = tk.Label(root , text= 'Wind Direction')
        self.wind_dir_lbl.place(relx = 0.96, rely = 0.25, anchor = 'ne')
        self.wind_dir_entry = tk.Entry(root, width= 25, state='readonly')
        self.wind_dir_entry.place(relx = 1, rely = 0.3, anchor = 'ne')
        ###__________________________row 3 end_________________________________###
        self.cond_entry_lbl = tk.Label(root , text= 'Weather Condition')
        self.cond_entry_lbl.place(relx = 0.47, rely = 0.35, anchor = 'ne')
        self.cond_entry = tk.Entry(root, width= 25, state='readonly')
        self.cond_entry.place(relx = 0.5, rely = 0.4, anchor = 'ne')

        self.max_temp_lbl = tk.Label(root , text= 'Max Temperature')
        self.max_temp_lbl.place(relx = 0.715, rely = 0.35, anchor = 'ne')
        self.max_temp_entry = tk.Entry(root, width= 25, state='readonly')
        self.max_temp_entry.place(relx = 0.75, rely = 0.4, anchor = 'ne')

        self.wind_gust_lbl = tk.Label(root , text= 'Wind Gust (mph)')
        self.wind_gust_lbl.place(relx = 0.96, rely = 0.35, anchor = 'ne')
        self.wind_gust_entry = tk.Entry(root, width= 25, state='readonly')
        self.wind_gust_entry.place(relx = 1, rely = 0.4, anchor = 'ne')
        ###__________________________row 4 end_________________________________###
        self.sunrise_lbl = tk.Label(root , text= 'Sunrise (date & time)')
        self.sunrise_lbl.place(relx = 0.47, rely = 0.45, anchor = 'ne')
        self.sunrise_entry = tk.Entry(root, width= 25, state='readonly')
        self.sunrise_entry.place(relx = 0.5, rely = 0.5, anchor = 'ne')

        self.pressure_lbl = tk.Label(root , text= 'Pressure (mm Hg)')
        self.pressure_lbl.place(relx = 0.72, rely = 0.45, anchor = 'ne')
        self.pressure_entry = tk.Entry(root, width= 25, state='readonly')
        self.pressure_entry.place(relx = 0.75, rely = 0.5, anchor = 'ne')

        self.humidity_lbl = tk.Label(root , text= 'Humidity')
        self.humidity_lbl.place(relx = 0.93, rely = 0.45, anchor = 'ne')
        self.humidity_entry = tk.Entry(root, width= 25, state='readonly')
        self.humidity_entry.place(relx = 1, rely = 0.5, anchor = 'ne')
        ###__________________________row 5 end_________________________________###
        self.sunset_lbl = tk.Label(root , text= 'Sunset (date & time)')
        self.sunset_lbl.place(relx = 0.47, rely = 0.55, anchor = 'ne')
        self.sunset_entry = tk.Entry(root, width= 25, state='readonly')
        self.sunset_entry.place(relx = 0.5, rely = 0.6, anchor = 'ne')
        ###__________________________row 6 end_________________________________###

        # Add zip code label inside of the root window
        self.zip_code_lbl = tk.Label(root , text= 'Zip Code')
        self.zip_code_lbl.place(relx = 0.125, rely = 0.105, anchor = 'sw')

        # Add zip code entry field
        self.zip_code_entry = tk.Entry(root , width= 15)
        self.zip_code_entry.place(relx = 0.1, rely = 0.15, anchor = 'sw')

        # Add country code label inside of the root window
        self.country_code_lbl = tk.Label(root , text= 'Country Code')
        self.country_code_lbl.place(relx = 0.105, rely = 0.205, anchor = 'sw')

        # Add country code entry field
        self.country_code_entry = tk.Entry(root , width= 15)
        self.country_code_entry.place(relx = 0.1, rely = 0.25, anchor = 'sw')
        self.country_code_entry.insert(-1 , 'us')

        # Add display text entry field
        self.textbox_entry = tk.Entry(root , width= 110)
        self.textbox_entry.place(relx = 0.5, rely = 0.95, anchor = 'center')
        self.textbox_entry.insert(-1 , 'Enter Zip Code and Country Code and select GET Data to get currentweather data via call to WeatherMap API Service')

        # Add button widget for getting data
        get_data_btn = tk.Button(root , text= 'GET Data' , fg= 'black' , bg='silver' , command=self.get_data, width= 12)
        get_data_btn.place(relx = 0.1, rely = 0.4, anchor = 'sw')

        # Add button widget for exiting
        exit_btn = tk.Button(root , text= 'Exit' , fg= 'red' , bg='silver' , command=exit, width= 12)
        exit_btn.place(relx = 0.1, rely = 0.5, anchor = 'sw')

    # Function definition for when GET Data button is clicked
    def get_data(self):
        file_data = self.read_configinfo_from_file()
        self.textbox_entry.insert(-1 , 'Fetching data from OpenWeatherMap API...')
        if file_data['API Key'] == '':
            print('Failed to read API key from the Weather Map App Settings.cfg file, application will now terminate.')

        else:
            full_url = self.form_full_url() # build the full URL for the API call
            try:
                print('\nFetching data from OpenWeatherMap API...')
                self.empty_weather_data_widgets()
                response = requests.get(full_url) # opening a network connection and fetching data
                if response.status_code == 200: # status code, success:200
                    self.weather_data = response.json()
                    self.populate_weather_data_widgets()
                    print(self.weather_data)
                else:
                    print('API request failed to return successfully.')
                    print('API response status code: ' , response.status_code)
                    print('API request failed to return successfully from the requested URL: ' , full_url)

            except:
                print('\nCould not access the requested URL.')
                print('Failed to reach: ' , full_url)
            self.textbox_entry.insert(-1 , 'Enter Zip Code and Country Code and select GET Data to get currentweather data via call to WeatherMap API Service')
        return
    
    def read_configinfo_from_file(self):
        # Use this function to read in the API key and temperature unit specifier from the .cfg file
        config = ConfigParser() # instantiate

        config.read(self.file_path) # parse existing file

        # read values from a section
        API_key_string = str(config.get('API Key', 'Value'))
        temp_unit_string = str(config.get('Temperature Unit', 'Value'))

        return {'API Key' : API_key_string, 'Temp Unit Specifier' : temp_unit_string}

    def form_full_url(self):
        file_data = self.read_configinfo_from_file()

        # full URL = base URL + zip code + ',' + country code + '&appid=' + API key + '&units=' + unit type
        full_url = str(self.base_url) + self.zip_code_entry.get() + ',' +  self.country_code_entry.get() + '&appid=' + file_data['API Key'] 
        full_url = full_url + '&units=' + file_data['Temp Unit Specifier']

        return full_url

    def populate_weather_data_widgets(self):
        hpa_to_mmHg_conversion_factor = 33.86389
        pressure_mmHg = str(round(float(self.weather_data['main']['pressure'])/hpa_to_mmHg_conversion_factor,2))
        utc_sunrise_time = (self.weather_data['sys']['sunrise'] + self.weather_data['timezone'])
        utc_sunset_time = (self.weather_data['sys']['sunset'] + self.weather_data['timezone'])
        temperature_unit = ''

        file_data = self.read_configinfo_from_file()
        if file_data['Temp Unit Specifier'] == 'standard': # (Kelvin)
            temperature_unit = '(Kelvin)'
        if file_data['Temp Unit Specifier'] == 'metric': # (Celsius)
            temperature_unit = '(deg C)'
        if file_data['Temp Unit Specifier'] == 'imperial': # (Farenheit)
            temperature_unit = '(deg F)'

        self.loc_entry.configure(state= 'normal')
        self.loc_entry.insert(-1, F"{self.weather_data['name']}, {self.weather_data['sys']['country']}")
        self.loc_entry.configure(state= 'readonly')

        self.geocoord_entry.configure(state= 'normal')
        self.geocoord_entry.insert(-1, F"{self.weather_data['coord']['lon']}, {self.weather_data['coord']['lat']}")
        self.geocoord_entry.configure(state= 'readonly')
        
        self.temp_entry.configure(state= 'normal')
        self.temp_entry.insert(-1, F"{temperature_unit}: {self.weather_data['main']['temp']}")
        self.temp_entry.configure(state= 'readonly')

        self.feels_like_entry.configure(state= 'normal')
        self.feels_like_entry.insert(-1, F"{temperature_unit}: {self.weather_data['main']['feels_like']}")
        self.feels_like_entry.configure(state= 'readonly')

        self.humidity_entry.configure(state= 'normal')
        self.humidity_entry.insert(-1, F"{self.weather_data['main']['humidity']}")
        self.humidity_entry.configure(state= 'readonly')

        self.max_temp_entry.configure(state= 'normal')
        self.max_temp_entry.insert(-1, F"{temperature_unit}: {self.weather_data['main']['temp_max']}")
        self.max_temp_entry.configure(state= 'readonly')

        self.min_temp_entry.configure(state= 'normal')
        self.min_temp_entry.insert(-1, F"{temperature_unit}: {self.weather_data['main']['temp_min']}")
        self.min_temp_entry.configure(state= 'readonly')

        self.temp_entry.configure(state= 'normal')
        self.pressure_entry.insert(-1, F"{pressure_mmHg}")
        self.temp_entry.configure(state= 'readonly')

        self.desc_entry.configure(state= 'normal')
        self.desc_entry.insert(-1, F"{self.weather_data['weather'][0]['description']}")
        self.desc_entry.configure(state= 'readonly')
        
        self.cond_entry.configure(state= 'normal')
        self.cond_entry.insert(-1, F"{self.weather_data['weather'][0]['main']}")
        self.cond_entry.configure(state= 'readonly')
        
        self.sunrise_entry.configure(state= 'normal')
        self.sunrise_entry.insert(-1, datetime.utcfromtimestamp(utc_sunrise_time).strftime('%Y-%m-%d %I:%M:%S') + 'AM')
        self.sunrise_entry.configure(state= 'readonly')
        
        self.sunset_entry.configure(state= 'normal')
        self.sunset_entry.insert(-1, datetime.utcfromtimestamp(utc_sunset_time).strftime('%Y-%m-%d %I:%M:%S') + 'PM\n')
        self.sunset_entry.configure(state= 'readonly')
        return

    def empty_weather_data_widgets(self):
        self.loc_entry.configure(state= 'normal')
        self.loc_entry.delete(0, tk.END)
        self.loc_entry.configure(state= 'readonly')

        self.geocoord_entry.configure(state= 'normal')
        self.geocoord_entry.delete(0, tk.END)
        self.geocoord_entry.configure(state= 'readonly')
        
        self.temp_entry.configure(state= 'normal')
        self.temp_entry.delete(0, tk.END)
        self.temp_entry.configure(state= 'readonly')

        self.feels_like_entry.configure(state= 'normal')
        self.feels_like_entry.delete(0, tk.END)
        self.feels_like_entry.configure(state= 'readonly')

        self.humidity_entry.configure(state= 'normal')
        self.humidity_entry.delete(0, tk.END)
        self.humidity_entry.configure(state= 'readonly')

        self.max_temp_entry.configure(state= 'normal')
        self.max_temp_entry.delete(0, tk.END)
        self.max_temp_entry.configure(state= 'readonly')

        self.min_temp_entry.configure(state= 'normal')
        self.min_temp_entry.delete(0, tk.END)
        self.min_temp_entry.configure(state= 'readonly')

        self.temp_entry.configure(state= 'normal')
        self.pressure_entry.delete(0, tk.END)
        self.temp_entry.configure(state= 'readonly')

        self.desc_entry.configure(state= 'normal')
        self.desc_entry.delete(0, tk.END)
        self.desc_entry.configure(state= 'readonly')
        
        self.cond_entry.configure(state= 'normal')
        self.cond_entry.delete(0, tk.END)
        self.cond_entry.configure(state= 'readonly')
        
        self.sunrise_entry.configure(state= 'normal')
        self.sunrise_entry.delete(0, tk.END)
        self.sunrise_entry.configure(state= 'readonly')
        
        self.sunset_entry.configure(state= 'normal')
        self.sunset_entry.delete(0, tk.END)
        self.sunset_entry.configure(state= 'readonly')    
        return 

if __name__ == '__main__':
   root = tk.Tk() # create root window
   main_app =  MainApplication(root, BASE_URL, FILE_PATH)
   root.mainloop() # execute tkinter GUI 









