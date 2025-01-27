# API-INTEGRATION-AND-DATA-VISUALIZATION
**COMPANY**: CODETECH IT SOLUTIONS
**NAME**: KHUSHI CHAUDHARY
**INTERN ID**:CT08IHY
**DOMAIN**: PYTHON
**BATCH DURATION**: DECEMBER 30TH,2024 TO JANUARY 30TH,2025
**MENTOR NAME**: NEELA SANTOSH
**DESCRIPTION**:
This Python script is a simple weather forecast application that uses the OpenWeatherMap API to fetch weather data for a given city and visualizes the temperature forecast for the next 24 hours. Here's a detailed explanation of the code:

1. Purpose of the Script
The script is designed to:

Retrieve weather forecast data for a user-specified city using the OpenWeatherMap API.
Parse and display temperature data for the next 24 hours in a tabular format.
Visualize this temperature forecast in a bar chart using the Matplotlib library.
2. Key Components and Functions
Imports
The script imports two Python libraries:

requests: Used to send HTTP requests to the OpenWeatherMap API and fetch JSON responses.
matplotlib.pyplot: Used for data visualization, specifically to create bar charts.
get_weather_data Function
This function retrieves weather data for a given city:

Inputs:
city: The name of the city the user is interested in.
api_key: The API key required to authenticate with the OpenWeatherMap API.
Steps:
Constructs the API endpoint URL with the city name, API key, and metric units for temperature (Celsius).
Sends an HTTP GET request to the API using requests.get.
Checks the response's status code. If it's 200 (success), the JSON response containing weather data is returned. If not, an error message is displayed.
Output:
Returns the weather data as a dictionary if the request is successful, or None if there’s an error.
visualize_weather Function
This function visualizes the temperature data:

Input: A dictionary of weather data fetched from the API.
Steps:
Extracts the date-time (dt_txt) and temperature (main['temp']) for the first 8 intervals (~24 hours) from the list field in the API response.
Plots a bar chart using Matplotlib with:
X-axis: Date and time.
Y-axis: Temperatures in Celsius.
Formats the chart for better readability (rotated X-axis labels and tighter layout).
Output: Displays a bar chart showing the temperature forecast.
main Function
This is the entry point of the script:

Prompts the user to input the city name.
Calls get_weather_data to fetch the weather forecast.
If the API request is successful:
Prints the date, time, and corresponding temperatures for the next 24 hours in the console.
Calls visualize_weather to generate a bar chart of the temperature forecast.
API Key
The script uses a placeholder API key (81c713f0e2a0392a57470fd3db0a0f0b). To use this script, you need to replace it with your valid OpenWeatherMap API key.

3. Execution Flow
When the script runs:

The user is prompted to input a city name.
The script calls get_weather_data to fetch weather data for the city.
If successful:
Weather data (date, time, and temperature) is printed to the console.
A bar chart visualizing the temperature forecast for the next 24 hours is displayed.
If the API call fails, the user is informed of the error.
4. Usage and Customization
API Key: Replace the placeholder key with your valid API key from OpenWeatherMap.
Time Intervals: The script processes 8 intervals (~24 hours) by default, as the API provides data at 3-hour intervals. You can increase or decrease this by modifying data['list'][:8].
Visualization: The bar chart can be styled further (e.g., adding gridlines, changing colors).

5. Practical Applications
This script demonstrates how to use external APIs and visualize data in Python. It can be expanded to include:

Multiple weather parameters (e.g., humidity, wind speed).
Additional cities for comparison.
A graphical user interface (GUI) for better interactivity.
This code is beginner-friendly and serves as a foundation for building more advanced weather apps.









