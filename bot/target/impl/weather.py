from bot.target.target import Target
from bot.utils.date_utility import get_date_object, get_week_day_str
from bot.utils.request_utility import get_json_from_request


class WeatherTarget(Target):

    def __init__(self):
        super().__init__()
        self.language = "ko-kr"

    def _retrieve_notifications(self):
        forecasts = []
        location_key = self.__get_location_key()
        data = self.__get_weather_forecast(location_key)

        for forecast in data["DailyForecasts"]:
            date = get_date_object(forecast["Date"], "%Y-%m-%dT%H:%M:%S%z").date()
            min_temp = forecast["Temperature"]["Minimum"]["Value"]
            max_temp = forecast["Temperature"]["Maximum"]["Value"]
            day_weather = forecast["Day"]["IconPhrase"]
            night_weather = forecast["Night"]["IconPhrase"]
            week_day = get_week_day_str(date)

            forecasts.append(f"{date} ({week_day}) - 낮: {day_weather}, 밤: {night_weather} / 최저 기온: {min_temp}°C, 최고 기온: {max_temp}°C")

        return forecasts

    def __get_location_key(self):
        params = {"apikey": self._config["apiKey"], "q": self._config["city"], "language": self.language}
        url = "http://dataservice.accuweather.com/locations/v1/cities/search"
        data = get_json_from_request(url, params)

        return data[0]["Key"]

    def __get_weather_forecast(self, location_key):
        params = {"apikey": self._config["apiKey"], "language": self.language, "metric": True}
        url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}"

        return get_json_from_request(url, params)