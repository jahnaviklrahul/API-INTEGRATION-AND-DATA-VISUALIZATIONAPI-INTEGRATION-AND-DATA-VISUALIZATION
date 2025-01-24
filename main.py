from fetch_weather import fetch_weather_data
from process_data import process_weather_data
from visualize_data import create_visualizations
import requests

# API Setup
API_KEY = "8953e3ced96a15b85a35e94531721eec"  # Replace with your valid API key
CITY = "Africa"  # You can use a specific city like "Delhi" or "Mumbai" for more precise data

# Main Script
if __name__ == "__main__":  # Corrected the if condition
    try:
        # Fetch and process data
        weather_data = fetch_weather_data(CITY, API_KEY)
        temp, feels_like, humidity, weather_desc = process_weather_data(weather_data)

        # Print weather description
        print(f"Weather in {CITY}: {weather_desc.capitalize()}")
        print(f"Temperature: {temp}°C, Feels Like: {feels_like}°C, Humidity: {humidity}%")

        # Create visualizations
        create_visualizations(temp, feels_like, humidity, CITY)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print("An error occurred:", e)

