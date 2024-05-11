# aerocast/__main__.py
from aerocast.weather import WeatherManager
from aerocast.airport import AirportManager
from aerocast.tts_manager import TextToSpeechManager

def main():
    print("Bienvenue dans AeroCast, votre gestionnaire de météo d'aéroport!")
    
    # Exemple d'utilisation des gestionnaires
    airport_code = "KJFK"  # Code OACI de l'aéroport Charles de Gaulle
    weather_manager = WeatherManager(airport_code)
    airport_manager = AirportManager(airport_code)
    
    # Récupérer les informations
    #print(weather_manager.summarize())
    print(weather_manager.get_temperature())
    #print(weather_manager.get_wind_speed())
    airport_info = airport_manager.get_airport_info()
    
    #print(airport_info.summarize())
    
    # Texte à parole pour les informations récupérées
    tts_weather = TextToSpeechManager(weather_manager.summarize())
    #tts_airport = TextToSpeechManager(airport_info.summarize())
    tts_weather.save_to_file("weather_info.mp3")
    #tts_airport.save_to_file("airport_info.mp3")
    
    print("Les informations ont été sauvegardées en audio.")

if __name__ == "__main__":
    main()