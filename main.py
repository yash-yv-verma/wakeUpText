#Imported appropriate APIs and libraries
import requests
from twilio.rest import Client
import random


# Twilio Account SID and Auth Token
accountSid = 'ACf7ef6d2757c5f1400fd5f48d9e82a1fd'
authToken = 'f9352989057b1c8366d62e6a011bb0ca'
client = Client(accountSid, authToken)


# Function to fetch a random motivational quote
def get_motivational_quote():
    response = requests.get('https://zenquotes.io/api/random')
    data = response.json()
    return data[0]['q']


# Function to fetch current weather data
def get_weather_info(apiKey, city):
    apiKey = "31d574b6404a4dd984142e7f7f393cf2"
    city = "Austin"
    try:
        baseUrl = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': apiKey}
        response = requests.get(baseUrl, params=params)
        response.raise_for_status()  # Raise an exception if the request is not successful
        data = response.json()

        # Check if weather key exists in the response
        if 'weather' in data and len(data['weather']) > 0:
            weather = data['weather'][0]['description']
        else:
            weather = 'Weather data not available'

        temperature = round(data['main']['temp'] - 273.15, 2)  # Convert to Celsius
        return f'{weather}, Temperature: {temperature}°C'
    except requests.exceptions.RequestException as e:
        return f'Failed to fetch weather data: {e}'


# Send the morning message
def send_morning_message():
    motivationalQuote = get_motivational_quote()
    weatherInfo = (get_weather_info('31d574b6404a4dd984142e7f7f393cf2', 'Austin')).upper()
    morningText = 'Good Morning, Yash!'

    text = f'\n\n{morningText} 🌞\n\nMotivational Quote:\n\n{motivationalQuote}\n\nWeather Insights:\n\n{weatherInfo}'

    client = Client(accountSid, authToken)

    mess = client.messages\
        .create(
        from_='+18337060072',
        body=text,
        to='+14012343229'

    )


#Initiates the SMS push
if __name__ == '__main__':
    send_morning_message()
    #print(mess.body)
