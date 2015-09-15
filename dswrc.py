#!/usr/bin/env python
# -*- coding: utf-8 -*-

# - - - Dead (simple) Weather options - - - #

# WOEID Code ** This is where you set your location. Visit woeid.factormystic.net for a list.
default_woeid = "1225448"

# Display Options ** 0 = Default output, 1 = custom output via 'custom_str' option below
display_opt = 1

# Custom String ** Display how you would like your weather data to be outputted
# 
# List of Vars:
# #title
# #link
# #lastupdate
# #sunrise
# #sunset
# #pressure
# #humidity
# #location_city
# #location_country
# #windspeed
# #temp
# #condition
# #conditioncode ** visit http://developer.yahoo.com/weather/ to see what each code means 
# #day(1 - 5)
custom_str = "Currently in #location_city\n#tempc and #condition\nTomrrow:\n#day1"

# Units of measure ** 'c' = celcius, 'f' = fahrenheit
units = 'c'
