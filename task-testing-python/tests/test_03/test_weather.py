import pytest
import requests_mock
from src.weather_03.weather_wrapper import *
from service import *


@pytest.fixture
def weather_wrapper():
    return WeatherWrapper('2751330')

def test_weather_1(weather_wrapper):
    with requests_mock.Mocker() as mock:
        mock.get(BASE_URL, json=base_moscow)
        mock.get(LOCATION_URL, json=location_moscow)
        mock.get(FORECAST_URL, text=str(forecast_moscow))

        mock.get(BASE_URL, json=base_samara)
        mock.get(LOCATION_URL, json=location_samara)
        mock.get(FORECAST_URL, text=str(forecast_samara))

        weather_wrapper.location_cache = {}
        mock.get(LOCATION_URL, json={}, status_code=200)
        with pytest.raises(ValueError):
            weather_wrapper.get_location_key("Moscow")
        mock.get(LOCATION_URL, json=location_moscow, status_code=200)

        weather_wrapper.location_cache = {"Moscow": "294021", "Samara": "567567"}
        mock.get(BASE_URL + "294021", json=base_moscow)
        assert weather_wrapper.get_temperature("Moscow") == 35.0

def test_weather_2(weather_wrapper):
    with requests_mock.Mocker() as mock:
        mock.get(BASE_URL, json=base_moscow)
        mock.get(LOCATION_URL, json=location_moscow)
        mock.get(FORECAST_URL, text=str(forecast_moscow))

        mock.get(BASE_URL, json=base_samara)
        mock.get(LOCATION_URL, json=location_samara)
        mock.get(FORECAST_URL, text=str(forecast_samara))

        weather_wrapper.get_response_city("Samara", LOCATION_URL)
        mock.get(LOCATION_URL, json=location_moscow, status_code=305)
        with pytest.raises(AttributeError) :
            weather_wrapper.get_response_city("Samara", LOCATION_URL)
        mock.get(LOCATION_URL, json=location_moscow, status_code=200)
        weather_wrapper.location_cache = {"Moscow": "294021"}
        assert weather_wrapper.get_location_key("Moscow") == "294021"


def test_weather_3(weather_wrapper):
    with requests_mock.Mocker() as mock:
        mock.get(BASE_URL, json=base_moscow)
        mock.get(LOCATION_URL, json=location_moscow)
        mock.get(FORECAST_URL, text=str(forecast_moscow))

        mock.get(BASE_URL, json=base_samara)
        mock.get(LOCATION_URL, json=location_samara)
        mock.get(FORECAST_URL, text=str(forecast_samara))

        weather_wrapper.location_cache = {"Moscow": "294021"}

        mock.get(BASE_URL + "294021", json=base_moscow)
        mock.get(FORECAST_URL + "294021", json=forecast_moscow)
        weather_wrapper.get_tomorrow_temperature("Moscow")
        assert weather_wrapper.find_diff_two_cities("Moscow", "Moscow") == 0


def test_weather_4(weather_wrapper):
    with requests_mock.Mocker() as mock:
        mock.get(BASE_URL, json=base_moscow)
        mock.get(LOCATION_URL, json=location_moscow)
        mock.get(FORECAST_URL, text=str(forecast_moscow))

        mock.get(BASE_URL, json=base_samara)
        mock.get(LOCATION_URL, json=location_samara)
        mock.get(FORECAST_URL, text=str(forecast_samara))

        mock.get(FORECAST_URL + "294021", json=forecast_moscow)
        mock.get(BASE_URL + "249021", json=base_moscow)
        mock.get(FORECAST_URL + "567567", json=forecast_samara)
        mock.get(BASE_URL + "567567", json=base_samara)

        mock.get(BASE_URL + "567567", json=base_samara)
        assert weather_wrapper.get_diff_string("Samara", "Moscow") == 'Weather in Samara is warmer than in Moscow by 0 degrees'
        assert weather_wrapper.get_diff_string("Moscow", "Samara") == 'Weather in Moscow is warmer than in Samara by 0 degrees'
        assert weather_wrapper.get_diff_string("Moscow", "Moscow") == 'Weather in Moscow is warmer than in Moscow by 0 degrees'

        mock.get(BASE_URL + "567567", json=base_samara_2)
        assert weather_wrapper.get_diff_string("Samara", "Moscow") == 'Weather in Samara is warmer than in Moscow by 0 degrees'

        mock.get(BASE_URL + "249021", json=base_moscow)
        mock.get(FORECAST_URL + "249021", json=forecast_moscow)
        assert weather_wrapper.get_tomorrow_diff("Moscow") == 'The weather in Moscow tomorrow will be much colder than today'

        mock.get(BASE_URL + "567567", json=base_samara_1)
        mock.get(FORECAST_URL + "567567", json=forecast_samara_1)
        assert weather_wrapper.get_tomorrow_diff("Samara") == 'The weather in Samara tomorrow will be the same than today' 

