def process_weather_data(data):
    """Extracts temperature, humidity, and description from the API response."""
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description']
    return temp,feels_like,humidity,weather_desc