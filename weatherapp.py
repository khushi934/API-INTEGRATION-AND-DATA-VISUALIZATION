import requests
import matplotlib.pyplot as plt

def get_weather_data(city, api_key):
    """
    Fetches weather data for a given city using OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data. Check your API key or city name.")
        return None

def visualize_weather(data):
    """
    Visualizes the temperature data from the weather API.
    """
    dates = []
    temperatures = []

    for item in data['list'][:8]:  # Getting data for 8 intervals (~24 hours)
        dates.append(item['dt_txt'])
        temperatures.append(item['main']['temp'])

    plt.figure(figsize=(10, 6))
    plt.bar(dates, temperatures, color='skyblue')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Forecast')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    city = input("Enter the city name: ")
    api_key = "81c713f0e2a0392a57470fd3db0a0f0b"
 #your OpenWeatherMap API key
    
    weather_data = get_weather_data(city, api_key)
    
    if weather_data:
        print(f"Weather forecast for {city}:")
        for item in weather_data['list'][:8]:
            print(f"{item['dt_txt']} - {item['main']['temp']}°C")
        
        visualize_weather(weather_data)

if __name__ == "__main__":
    main()








