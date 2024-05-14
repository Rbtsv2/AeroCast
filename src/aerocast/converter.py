def name_converter(name: str) -> str:
    return name.split(',')[0].strip()

def distance_converter(distance: (str, float)) -> (str, float):
    if isinstance(distance, float):
        return round(distance * 1.60934, 2)
    else:
        return distance

def temp_converter(temp: int) -> (int, float):
    return temp + 283.15