# Dead Simple Weather

## What is this?

This grabs weather data from Yahoo's [weather API](https://developer.yahoo.com/weather/) using [YQL](https://developer.yahoo.com/yql/) and allows you to format an output.

## Usage

    app.py (optional) "location" "string message"

## Settings

See `settings.py` for example.

Set `userstring` and/or `location` to `False` to specify in command line arguements. Eg.

    app.py "New York" "The current temp is #current_temp"

String substitution list

* #sunrise 
* #sunset
* #humidity
* #condition_code https://developer.yahoo.com/weather/documentation.html#codes
* #last_update
* #current_temp
* #forecast_high
* #forecast_low
* #current_condition
* #title
* #city
* #country
* #region

## Example Output

    user_string='''Current Temp in #city (#region) is #current_temp with a high of #forecast_high and a low of #forecast_low''' 

Output

    Current Temp in Melbourne (Victoria) is 14.4° with a high of 16.4° and a low of 6.7°

## Author

[James Bos](https://www.jamesbos.com)