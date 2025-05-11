import pytest
from unittest import mock
from ..collect_data import collect_weather_data
import requests
import csv
from datetime import datetime

# Mock the external API response
mock_response = {
    "main": {
        "temp": 25,
        "humidity": 60
    },
    "wind": {
        "speed": 10
    },
    "weather": [{
        "main": "Clear"
    }]
}

# Test case for collect_weather_data function
@mock.patch("requests.get")
@mock.patch("csv.DictWriter")
def test_collect_weather_data(mock_csv_writer, mock_requests_get):
    # Mock the response from the API
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = mock_response
    
    # Mock the CSV writer to avoid file operations
    mock_csv_instance = mock.Mock()
    mock_csv_writer.return_value = mock_csv_instance

    # Call the function
    collect_weather_data()

    # Assert that the requests.get was called with the correct URL
    mock_requests_get.assert_called_once_with(
        "http://api.openweathermap.org/data/2.5/weather?q=Karachi&appid=784b3f4a2e51848bf18cdef7604e4688&units=metric"
    )

    # Check that the writerow method was called once with the correct weather data
    weather_data = {
        "datetime": datetime.now().isoformat(),
        "temperature": 25,
        "humidity": 60,
        "wind_speed": 10,
        "condition": "Clear"
    }

    # Ensure that the CSV writer's `writerow` method is called with the correct data
    mock_csv_instance.writerow.assert_called_once_with(weather_data)

    # Ensure that the header is written only once (i.e., when the file is empty)
    mock_csv_instance.writeheader.assert_called_once()

