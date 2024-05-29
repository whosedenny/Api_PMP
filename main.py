import requests

class WeatherData:
    def __init__(self, location, temperature, condition, wind_speed, humidity):
        self.location = location
        self.temperature = temperature
        self.condition = condition
        self.wind_speed = wind_speed
        self.humidity = humidity

    def __str__(self):
        return (f"Weather in {self.location}:\n"
                f"Temperature: {self.temperature}°C\n"
                f"Condition: {self.condition}\n"
                f"Wind Speed: {self.wind_speed} kph\n"
                f"Humidity: {self.humidity}%")

def get_weather(api_key, location):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    response = requests.get(url)
    data = response.json()

    location_name = data['location']['name']
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']
    wind_speed = data['current']['wind_kph']
    humidity = data['current']['humidity']

    return WeatherData(location_name, temperature, condition, wind_speed, humidity)

# 'YOUR_API_KEY' - My API and Location
api_key = '77f8b518cee24856b9a101040242905'
location = 'Odesa'

weather_data = get_weather(api_key, location)
print(weather_data)
