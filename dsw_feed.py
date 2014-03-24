#!/usr/bin/env python
# -*- coding: utf-8 -*-

# - - - Dead (simple) Weather - - - - - - - - - - #
# This is a simple CLI based weather Application
# based on the FeedParser Python Module.
#
# This utilises the yahoo weather rss feed. I 
# cannot garauntee it will work forever.  
#
# License:
# GNU Public License (GPLv2)
# 
# Original Author:
# imadev@jamesbos.com 
# - - - - - - - - - - - - - - - - - - - - - - - - #

import feedparser
import sys
import bleach
import dswrc
import re

# if our command line argument exists, use the passed WOEID otherwise use the default WOEID
if len(sys.argv) == 1:
	location_woeid = dswrc.default_woeid
else:
	location_woeid = str(sys.argv[1])

# Yahoo RSS Url
feed_url = "http://weather.yahooapis.com/forecastrss?w={}&u={}".format(location_woeid,dswrc.units)

# Our main Application
def app(feed_url,opt):
	weather_feed = feedparser.parse(feed_url)
	title = weather_feed.feed.title
	link = weather_feed.feed.link
	lastupdate = weather_feed.feed.updated
	sunrise = weather_feed.feed.yweather_astronomy['sunrise']
	sunset = weather_feed.feed.yweather_astronomy['sunset']
	pressure = weather_feed.feed.yweather_atmosphere['pressure']
	humidity = weather_feed.feed.yweather_atmosphere['humidity']
	location_city = weather_feed.feed.yweather_location['city']
	location_country = weather_feed.feed.yweather_location['country']
	windspeed = weather_feed.feed.yweather_wind['speed']
	temp = weather_feed.entries[0]['yweather_condition']['temp']
	condition = weather_feed.entries[0]['yweather_condition']['text']
	conditioncode = weather_feed.entries[0]['yweather_condition']['code']
	forecast_data = weather_feed.entries[0]['description'] # sanitize our forecast data into something usable
	forecast_data = bleach.clean(forecast_data, strip=True).split('\n') # This clears out the HTML and splits into clearlines for each \n

	def forecast(day):
		fc_list = []
		for line in forecast_data:
			fc_list.append(line) # Add each line into array so we can pull what we want
		
		if day == 1:
			return fc_list[4]
		elif day == 2:
			return fc_list[5]
		elif day == 3:
			return fc_list[6]
		elif day == 4:
			return fc_list[7]
		elif day == 5:
			return fc_list[8]
		else:
			all_days = "{}\n{}\n{}\n{}\n{}".format(fc_list[4],fc_list[5],fc_list[6],fc_list[7],fc_list[8])
			return all_days

	def custom_out(string):
		string = re.sub("#title", title, string)
		string = re.sub("#link", link, string)
		string = re.sub("#lastupdate", lastupdate, string)
		string = re.sub("#sunrise", sunrise, string)
		string = re.sub("#sunset", sunset, string)
		string = re.sub("#pressure", pressure, string)
		string = re.sub("#humidity", humidity, string)
		string = re.sub("#location_city", location_city, string)
		string = re.sub("#location_country", location_country, string)
		string = re.sub("#windspeed", windspeed, string)
		string = re.sub("#temp", temp, string)
		string = re.sub("#condition", condition, string)
		string = re.sub("#conditioncode", conditioncode, string)
		string = re.sub("#day1", forecast(1), string)
		string = re.sub("#day2", forecast(2), string)
		string = re.sub("#day3", forecast(3), string)
		string = re.sub("#day4", forecast(4), string)
		string = re.sub("#day5", forecast(5), string)
		return string
	
	# Default Output
	location_line_len = len(str(location_city + location_country)) + 28
	location_line_len = '-'*location_line_len
	full_summary = "{}\n| CURRENT CONDITIONS IN {}, {} |\n{}\nCurrent Conditions: {}\nCurrent Temp: {}c\nCurrent Humidity: {}%\n\n FORECAST\n{}\n{}\n\n LAST UPDATE\n{}\n{}".format(location_line_len,location_city,location_country,location_line_len,condition,temp,humidity,location_line_len,forecast(0),location_line_len,lastupdate)
	
	app_options = {
		0 : full_summary,
		1 : custom_out(dswrc.custom_str),
	}

	if opt in range(0,2):
		print app_options[opt]
	else: 
		print "No Display Option passed, using default..."
		print app_options[0]
# main app function
app(feed_url,dswrc.display_opt)