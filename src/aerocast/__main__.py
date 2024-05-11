# aerocast/__main__.py
from aerocast.weather import WeatherManager
from aerocast.airport import AirportManager


def main():
    print("Bienvenue dans AeroCast, votre gestionnaire de météo d'aéroport!")
    
    # Exemple d'utilisation des gestionnaires
    airport_code = "KJFK"  # Code OACI de l'aéroport Charles de Gaulle
    lang = "fr"

    weather = WeatherManager(airport_code, lang)

    print(weather.get_temperature())


    # airport_manager = AirportManager(airport_code)
    
    # Récupérer les informations
    #print(weather_manager.summarize())
   

    #print(weather_manager.get_wind_speed())
    # airport_info = airport_manager.get_airport_info()
    
    # print(airport_manager.summarize())
    

 

if __name__ == "__main__":
    main()