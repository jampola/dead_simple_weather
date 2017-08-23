# -*- coding: utf-8 -*-
import urllib, json, sys, re
import settings

class WeatherData(object):
	def __init__(self):
		self.url = "https://query.yahooapis.com/v1/public/yql?q="
		self.format = "&format=json"
		self.celcius = settings.celcius

		if settings.location:
			self.location = settings.location
		else:
			self.location = sys.argv[1]

		if settings.user_string:
			self.user_string = settings.user_string
		else:
			self.user_string = sys.argv[2]

		self.query = '''
			select * from weather.forecast 
			where woeid in (select woeid from geo.places(1) 
			where text='{}')'''\
			.format(self.location) 

		self.resp = urllib.urlopen(self.url+self.query+self.format)
		self.data = json.loads(self.resp.read())['query']['results']['channel']

	def convert_units(self, f):
		if self.celcius:
			return str(round((int(f) - 32) * 5.0/9.0, 1))+unicode('°', 'utf-8')
		else:
			return f+unicode('°F', 'utf-8')

	def grab_fields(self):
		weather_fields = dict(
			current_temp = \
				self.convert_units(self.data['item']['condition']['temp']),
			forecast_high = \
				self.convert_units(self.data['item']['forecast'][0]['high']),
			forecast_low = \
				self.convert_units(self.data['item']['forecast'][0]['low']),
			sunrise = self.data['astronomy']['sunrise'],
			sunset = self.data['astronomy']['sunset'],
			humidity = self.data['atmosphere']['humidity'],
			condition_code = self.data['item']['condition']['code'],
			last_update = self.data['item']['condition']['date'],
			current_condition = self.data['item']['condition']['text'],
			title = self.data['item']['title'],
			city = self.data['location']['city'],
			country = self.data['location']['city'],
			region = self.data['location']['city'],
		)
		return weather_fields

	def make_string(self):
		data = self.grab_fields()
		for x in data:
			self.user_string = re.sub("#"+x, data[x], self.user_string)
		return self.user_string

def main():
	weather = WeatherData().make_string()
	sys.stdout.write(weather)

if __name__ == '__main__':
	main()