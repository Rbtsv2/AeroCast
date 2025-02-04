# aerocast/__main__.py
from aerocast.weather import WeatherManager
from aerocast.airport import AirportManager
import gettext, locale, argparse

def main():
    parser = argparse.ArgumentParser(prog='AeroCast', description='A program for providing weather information for airports.')
    parser.add_argument('OACI')
    parser.add_argument('-l', '--lang', default=None)
    parser.add_argument('-p', '--play', action='store_true', help='Generate and play the audio for the summary')

    args = parser.parse_args()

    language = locale.getlocale()[0].split('_')[0]
    chosen_language = args.lang or language
    default_lang = gettext.translation('messages', 'locales', languages=[chosen_language], fallback=True)
    default_lang.install()

    print(_("Welcome to AeroCast, your airport weather manager!"))
    wm = WeatherManager(args.OACI, lang=chosen_language)
    summary = wm.get_summarize()
    print(summary)

    if args.play:
        wm.play_text(summary)

    #wm.get_wind_speed()
    #wm.get_temperature()

    #airport_manager = AirportManager(airport_code)

if __name__ == "__main__":
   main()