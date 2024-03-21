import tkinter as tk
import requests


API_KEY = "5aaf4dfbc5d8a567d91ee612c16a7cd0"

def get_weather_data(city):
    """Fetches weather data from OpenWeatherMap API for the specified city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

def display_weather(data):
    """Displays weather data in a user-friendly format on the GUI."""
    if data is None:
        weather_label.config(text="Error retrieving weather data.")
        return

    city = data["name"]
    temperature = kelvin_to_celsius(data["main"]["temp"])
    feels_like = kelvin_to_celsius(data["main"]["feels_like"])
    weather_description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    weather_label.config(text=f"City: {city}\nTemperature: {temperature:.2f}°C (Feels Like: {feels_like:.2f}°C)\nWeather: {weather_description}\nHumidity: {humidity}%")

def kelvin_to_celsius(kelvin):
    """Converts Kelvin temperature to Celsius."""
    return kelvin - 273.15

def update_weather():
    """Retrieves weather data for the entered city and displays it."""
    city = city_entry.get()
    weather_data = get_weather_data(city)
    display_weather(weather_data)


root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter City:")
city_label.pack(padx=10, pady=5)

city_entry = tk.Entry(root)
city_entry.pack(padx=10, pady=5)

weather_label = tk.Label(root, text="", font=("Arial", 12))
weather_label.pack(padx=10, pady=15)


update_button = tk.Button(root, text="Get Weather", command=update_weather)
update_button.pack(padx=10, pady=5)

root.mainloop()
