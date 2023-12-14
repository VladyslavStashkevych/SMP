import sys

from src.Core.WeatherForecastApiClient import WeatherForecastClient
from src.UI.MenuBuilder import *
from src.UI.MenuItem import *


gen = WeatherForecastClient()

output_json = MenuItem("1", "Get output in json format", print, [gen.call_client])
output_text = MenuItem("2", "Get output in text format", print, [gen.get_text])
output_menu = MenuBuilder([output_json, output_text])

get_weather = MenuItem("1", "Get weather.", output_menu.initialize)
change_city = MenuItem("2", "Change city.", gen.change_city)
change_lang = MenuItem("3", "Change language of a forecast.", gen.change_language)
change_days = MenuItem("4", "Change days of a forecast.", gen.change_days)

exit_menu = MenuItem("9", "Exit.", sys.exit)
weather_menu = MenuBuilder([get_weather, change_city, change_lang, change_days, exit_menu])


def main():
    while True:
        weather_menu.initialize()


if __name__ == "__main__":
    main()
