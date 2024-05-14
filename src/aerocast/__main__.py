# aerocast/__main__.py
from aerocast.weather import WeatherManager
from aerocast.airport import AirportManager
import gettext, locale

lang_translations = gettext.translation('messages', localedir='locales', fallback=True)
_ = lang_translations.gettext

def main():

    print(_("Welcome to AeroCast, your airport weather manager!"))
    
    # Exemple d'utilisation des gestionnaires
    airport_code = "KJFK"  # Code OACI de l'aéroport Charles de Gaulle
    lang = "fr"

    weather = WeatherManager(airport_code) # , lang
    summary = weather.get_summarize()
    print(summary)
    weather.play_text(summary)
    #weather.get_wind_speed()
    #weather.get_temperature()

    #airport_manager = AirportManager(airport_code)

if __name__ == "__main__":
    main()