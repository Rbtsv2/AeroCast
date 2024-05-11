# aerocast/airport.py
class AirportManager:
    def __init__(self, data):
        self.data = data

    def summarize(self):
        return f"Airport: {self.data['name']} Location: {self.data['location']}"