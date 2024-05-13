from colorama import Fore, Back, Style
import os
from playsound3 import playsound
import re
import json
from datetime import datetime
import time
import locale

from .api import API

try:
    from gtts import gTTS
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print("atc.meteo : Impossible d'importer les modules nécessaires." + str(e))
    os.system("pause")
    exit()

locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')
DATA_PROVIDER = "https://aviationweather.gov"

FIELDNAMES = ['metar_id', 'icaoId', 'receiptTime', 'obsTime', 'reportTime', 'temp', 'dewp', 'wdir', 'wspd', 'visib', 'altim', 'lat', 'lon', 'elev', 'lat', 'lon', 'elev', 'prior', 'name', 'rawOb', 'clouds']

def info(OACI)->bool:
    print(Fore.GREEN + "✅ CHARGEMENT DU MODULE METEO" + Style.RESET_ALL)

    # Obtenir les données météo et les informations sur l'aéroport
    weather_data = get_meteo(OACI)  
    airport_info = get_airport_info(OACI)
    taf_info = get_taf(OACI)

    airport_text = f"Bienvenue à l'aéroport de {airport_info['Name'].lower()}. " \
                   f"Latitude: {airport_info['Latitude']}, Longitude: {airport_info['Longitude']}. " \
                   f"Elevation: {airport_info['Elevation']} mètres au-dessus du niveau de la mer. " \
                   f"Il y a {len(airport_info['Runways'])} pistes sur cet aéroport. "

    meteo_text = f"le METAR indique un vent de {weather_data['wdir']} degrés, avec une vitesse de {weather_data['wspd']} nœuds, " \
                 f"D'après les codes de temps nous avons un {weather_data['clouds']}, ce qui signifie des conditions temporaires {weather_data['clouds_text']}." \
                 f"La distance de visibilité est de {weather_data['visib']} kilomètres, " \
                 f"la température est de {weather_data['temp']} degrés Celsius, et le point de rosée est de {weather_data['dewp']} degrés Celsius." \
                 f"La pression atmosphérique QNH est situé à {weather_data['altim']} hPa" 

    taf_text = (
        f"Des prévisions météorologiques plus précises nous ont été émises par le taf le {taf_info['issued']}. Il seront valide du {taf_info['valid_from']} au {taf_info['valid_to']}. "
     
    )

    # Ajout des prévisions détaillées pour chaque période
    for index, forecast in enumerate(taf_info['forecast']):
   
        # Spécifiquement pour les changements mentionnés dans les périodes suivantes
        if index == 0:  # La seconde période
            taf_text += (
                f"À partir de {forecast['from_time']} les vents variront à {forecast['wind_speed']} nœuds avec une visibilité de {forecast['visibility']} kilomètres  et seront de direction {forecast['wind_direction']} "
                f"avec une couverture {forecast['clouds']}. "
            )
        if index == 1:  # La troisième période
            taf_text += (
                f"{forecast['speach'].lower()}."
                f"Les vents seront de direction {forecast['wind_direction']} à {forecast['wind_speed']} nœuds avec une visibilité de {forecast['visibility']} kilomètres"
                
            )


    report = f"Vous pourrez décoller en toute tranquilité, nos équipes et moi même vous souhaitons un bon vol !"
              
    meteo_tts = gTTS(meteo_text, lang="fr", slow=False)
    meteo_tts.save("meteo.mp3")

    airport_tts = gTTS(airport_text, lang="fr", slow=False)
    airport_tts.save("airport.mp3")

    airport_taf = gTTS(taf_text, lang="fr", slow=False)
    airport_taf.save("taf.mp3")

    airport_tts = gTTS(report, lang="fr", slow=False)
    airport_tts.save("report.mp3")

    playsound("Sounds/radio_deb.mp3")
    playsound("airport.mp3")
    playsound("Sounds/radio_fn.mp3")
    playsound("meteo.mp3")
    playsound("Sounds/radio_fn.mp3")
    playsound("taf.mp3")
    playsound("Sounds/radio_fn.mp3")
    playsound("report.mp3")
    playsound("Sounds/radio_fn.mp3")

    print(Fore.GREEN + f"✅ METAR {airport_info['Name']}: {weather_data['rawOb']}" + Style.RESET_ALL)

def extract_taf(raw_data):
    # Conversion de la chaîne JSON en dictionnaire Python
    data = json.loads(raw_data)
    taf = data[0]  # On suppose que le premier élément contient le TAF

    # Formatage correct des dates issues des chaînes de caractères
    date_format = "%Y-%m-%d %H:%M:%S"  # Assurez-vous que ce format correspond au format de vos dates
    issue_time = datetime.strptime(taf['issueTime'], date_format) if isinstance(taf['issueTime'], str) else datetime.utcfromtimestamp(taf['issueTime'])
    valid_from_time = datetime.strptime(taf['validTimeFrom'], date_format) if isinstance(taf['validTimeFrom'], str) else datetime.utcfromtimestamp(taf['validTimeFrom'])
    valid_to_time = datetime.strptime(taf['validTimeTo'], date_format) if isinstance(taf['validTimeTo'], str) else datetime.utcfromtimestamp(taf['validTimeTo'])

    response = {
        'airport': f"{taf['name']} ({taf['icaoId']})",
        'issued': issue_time.strftime('%A %d %B %Y %H:%M:%S UTC'),
        'valid_from': valid_from_time.strftime('%A %d %B %Y %H:%M UTC'),
        'valid_to': valid_to_time.strftime('%A %d %B %Y %H:%M UTC'),
        'forecast': []
    }

    # Extraction des prévisions
    for forecast in taf['fcsts']:
        from_time = datetime.strptime(forecast['timeFrom'], date_format) if isinstance(forecast['timeFrom'], str) else datetime.utcfromtimestamp(forecast['timeFrom'])
        to_time = datetime.strptime(forecast['timeTo'], date_format) if isinstance(forecast['timeTo'], str) else datetime.utcfromtimestamp(forecast['timeTo'])
        
        if isinstance(forecast['visib'], float):
            # La visibilité est en miles, on la convertit en kilomètres
            forecast['visib'] = round(forecast['visib'] * 1.60934, 2)

        if forecast['wdir'] == "VRB":
            forecast['wdir'] = "variables"
        else:
            forecast['wdir'] = str(forecast['wdir']) + "°"

        
        forecast_entry = {
            'from_time': from_time.strftime('%A %d %B %Y %H:%M UTC'),
            'to_time': to_time.strftime('%A %d %B %Y %H:%M UTC'),
            'wind_direction': forecast['wdir'],
            'wind_speed': forecast['wspd'],
            'visibility': forecast['visib'],
            'fcstChange': traduire_abreviation(forecast['fcstChange']),
            'clouds': ", ".join([
                f"{traduire_abreviation(cloud['cover'])}" +
                (f" à {cloud['base']} pieds" if cloud['base'] is not None else "") +
                (f" ou {cloud['base'] * 0.0003048:.2f} kilomètres" if cloud['base'] is not None else "")
                for cloud in forecast['clouds']
            ]),
            'speach' : traduire_abreviation(forecast['fcstChange'], traduire_abreviation(forecast['wxString']), forecast['probability'], from_time.strftime('%A %d %B %Y %H:%M UTC'))
        
        }
        response['forecast'].append(forecast_entry)
    
    return response

def get_taf(airport)->tuple:
    """
    Permet de créer un tuple contenant les informations météos de l'aéroport
    Pré  : str : code OACI de l'aéroport
    Post : tuple contenant : le cap du vent, la vitesse du vent, la pression atmosphérique (qnh) en hPa
    """
    url = f"{DATA_PROVIDER}/api/data/taf?ids={airport}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        # print(response.text)
        # exit()
        if response.text == '[]':
            print(Fore.YELLOW + "Aucune donnée TAF trouvée dans la réponse, nous allons essyer une autre approche" + Style.RESET_ALL)
            exit()
        airport_info = extract_taf(response.text)
    else:
        print(f"Erreur lors de la récupération des informations météo. (Code d'erreur : {response.status_code})")
        return ("000","0","1013 hPa")
    return airport_info

def get_airport_info(airport)->tuple:
    """
    Permet de créer un tuple contenant les informations météos de l'aéroport
    Pré  : str : code OACI de l'aéroport
    Post : tuple contenant : le cap du vent, la vitesse du vent, la pression atmosphérique (qnh) en hPa
    """
    url = f"{DATA_PROVIDER}/api/data/airport?ids={airport}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        #print(response.text)
        if response.text == '[]':
            print(Fore.YELLOW + "Aucune donnée trouvée dans la réponse, nous allons essyer une autre approche" + Style.RESET_ALL)
            exit()
        airport_info = extract_airport_info(response.text)
    else:
        print(f"Erreur lors de la récupération des informations météo. (Code d'erreur : {response.status_code})")
        return ("000","0","1013 hPa")
    return airport_info

def get_meteo(airport: str)->tuple:
    """
    Permet de créer un tuple contenant les informations météos de l'aéroport
    Pré  : str : code OACI de l'aéroport
    Post : tuple contenant : le cap du vent, la vitesse du vent, la pression atmosphérique (qnh) en hPa
    """
    #https://aviationweather.gov/api/data/airport?ids=LFBO info airport
    try:
        api = API()
        metar_data = API.get_metar_data(airport)
        metar_info = extract_metar_info(metar_data)
        return metar_info
    except Exception as e:
        raise

def extract_metar_info(data: dict):
    # Extraire les informations directement accessibles
    metar_info = {k:v for k,v in metar_data.items()}

    metar_info['name'] = metar_data['name'].split(',')[0].strip()

    visibility_miles = metar_data['visib']
    if isinstance(visibility_miles, float):
        # La visibilité est en miles, on la convertit en kilomètres
        visibility_km = round(visibility_miles * 1.60934, 2)
        metar_info['visib'] = visibility_km
    else:
        # La visibilité est sous forme de texte, on la conserve telle quelle
        metar_info['visib'] = visibility_miles

    metar_info['clouds'] = data['clouds'][0]['cover']
    metar_info['clouds_base'] = data['clouds'][0]['base']
    metar_info['clouds_text'] = traduire_abreviation(data['clouds'][0]['cover'])

    return metar_info

def traduire_abreviation(abreviation, conditions_meteo="", probabilite="", heure=""):
    abreviations = {
        "SKC": "d'un ciel dégagé",
        "CLR": "d'un ciel clair",
        "FEW": "de quelques nuages de 1 à 2 octas",
        "SCT": "de nuages épars de 3 à 4 octas",
        "BKN": "de nuages fragmentés de 5 à 7 octas",
        "OVC": "d'un Ciel couvert (8 octas)",
        "VV": "d'un ciel invisible en dessous de la base des nuages",
        "CB": "de cumulonimbus",
        "TCU": "de cumulus congestus",
        "CAVOK": "d'un ciel et visibilité clairs",
        "NSW": "sans précipitations importantes, pas de temps significatif",
        "FG": "de brouillard",
        "BR": "de brume",
        "HZ": "de brume sèche",
        "FU": "de fumée",
        "DU": "de poussière",
        "SA": "de sable",
        "VA": "de cendres volcaniques",
        "SQ": "de ligne de grains",
        "FC": "de tornade en formation",
        "TS": "d'orages",
        "SH": "d'averses",
        "DZ": "de bruine",
        "RA": "de pluie",
        "SN": "de neige",
        "SG": "de grésil",
        "IC": "de grésil en suspension",
        "PL": "de pluie verglaçante",
        "GR": "de grêle",
        "UP": "inconnues",
        "NSC": "sans nuages",

        "TEMPO": f"Ensuite, dès {heure} attendez-vous à des conditions temporaires {conditions_meteo} pendant une courte période.",
        "BECMG": f"Ensuite, dès {heure} prévoyez un changement et attendez-vous à des conditions temporaires {conditions_meteo} dans un avenir proche.",
        "PROB": f"Ensuite, dès {heure} il y a une probabilité de {probabilite}% {conditions_meteo} dans la période spécifiée.",
        "FM": f"Ensuite, à partir de {heure} attendez-vous à des conditions temporaires {conditions_meteo}.",
        "TL": f"Ensuite, jusqu'à {heure} attendez-vous à des conditions temporaires {conditions_meteo}.",
        "AT": f"Ensuite, à {heure} attendez-vous à des conditions temporaires {conditions_meteo}."
    }

    return abreviations.get(abreviation, "inconnue")

def extract_airport_info(raw_json):
    # Charger les données JSON
    data = json.loads(raw_json)

    # Récupérer les informations sur l'aéroport
    airport_info = {}
    airport_data = data[0]

    airport_info["Name"] = airport_data["name"]
    airport_info["IATA/FAA"] = airport_data["iata"]
    airport_info["Type"] = airport_data["type"]
    airport_info["Latitude"] = airport_data["lat"]
    airport_info["Longitude"] = airport_data["lon"]
    airport_info["Elevation"] = airport_data["elev"]
    airport_info["Source"] = airport_data["source"]
    airport_info["State"] = airport_data["state"]
    airport_info["Country"] = airport_data["country"]
    airport_info["Mag Declination"] = airport_data["mag_dec"]
    airport_info["Use"] = airport_data["use"]
    airport_info["Services"] = airport_data["services"]
    airport_info["Tower"] = airport_data["tower"]
    airport_info["Beacon"] = airport_data["beacon"]
    airport_info["Passengers"] = airport_data["passengers"]

    # Récupérer les informations sur les pistes
    runways_info = []
    for runway_data in airport_data["runways"]:
        runway_info = {
            "Number": runway_data["id"],
            "Dimension": runway_data["dimension"],
            "Surface": runway_data["surface"],
            "Alignment": int(runway_data["alignment"])
        }
        runways_info.append(runway_info)
    airport_info["Runways"] = runways_info

    # Récupérer les informations sur les fréquences
    frequencies_info = []
    for freq_data in airport_data["freqs"]:
        frequency_info = {
            "Type": freq_data["type"],
            "Frequency": float(freq_data["freq"])
        }
        frequencies_info.append(frequency_info)
    airport_info["Frequencies"] = frequencies_info

    return airport_info

if __name__ == '__main__':
    info('KJFK')