from collections import UserDict

class Celsius:
    '''Descriptor for celsius.'''

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    '''Descriptor for fahrenheit.'''

    def __get__(self, instance, owner):
        return instance.celsius * 1.8 + 32

    def __set__(self, instance, value):
        instance.celsius = (float(value) - 32) / 1.8


class Kelvin:
    '''Descriptor for kelvin.'''

    def __get__(self, instance, owner):
        return instance.celsius + 273.15

    def __set__(self, instance, value):
        instance.celsius = float(value) - 273.15


class Temperature:
    '''Class to represent temperature three descriptors for celsius and fahrenheit and kelvin'''
    celsius = Celsius()
    fahrenheit = Fahrenheit()
    kelvin = Kelvin()

class Meter:
    '''Descriptor for a meter.'''

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Kilometer:
    '''Descriptor for a centimeter.'''

    def __get__(self, instance, owner):
        return instance.meter / 1000

    def __set__(self, instance, value):
        instance.meter = float(value) * 1000

class Mile:
    '''Descriptor for a centimeter.'''

    def __get__(self, instance, owner):
        return instance.kilometer / 1.60934

    def __set__(self, instance, value):
        instance.kilometer = float(value) * 1.60934

class Foot:
    '''Descriptor for a foot.'''

    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance:
    '''Class to represent distance holding two descriptors for feet and meters.'''
    meter = Meter()
    kilometer = Kilometer()
    mile = Mile()
    foot = Foot()

def name_converter(name: str) -> str:
    return name.split(',')[0].strip()

def distance_converter(distance: (str, float)) -> (str, float):
    if isinstance(distance, float):
        return round(distance * 1.60934, 2)
    else:
        return distance

def temp_converter(temp: int) -> (int, float):
    return temp + 283.15

FIELDNAME_UNITS = {'temp': Temperature, 'visib': Distance}

class ConverterDict(UserDict):
    """docstring for ClassName"""
    def __init__(self, dict=None):
        UserDict.__init__(self, dict)

    def __getitem__(self, attr):
        if attr in self.data:
            return self.data[attr]
        else:
            attr, unit = attr.split('_', 2)
            converter = FIELDNAME_UNITS[attr]()
            converter.celsius = self.data[attr]
            if hasattr(converter, unit):
                return round(getattr(converter, unit), 2)
        raise KeyError