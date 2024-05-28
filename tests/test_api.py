# tests/test_api.py
import unittest
from aerocast.api import API

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_metar_data(self):
        api = API()
        data = api.get_metar_data('KJFK')
        self.assertIsInstance(data, dict)

    def test_airport_data(self):
        api = API()
        data = api.get_airport_data('KJFK')
        self.assertIsInstance(data, (dict, list))

    def test_airport_data_with_iata(self):
        api = API()
        data = api.get_airport_data('CDG')
        self.assertIsInstance(data, (dict, list))

    def test_fetch_metar(self):
        api = API()
        data = API.fetch_data('data/metar', {'ids': 'KJFK', 'format': 'json'})
        data2 = api.get_metar_data('KJFK')
        self.assertIsInstance(data, (dict, list))
        self.assertIsInstance(data2, (dict, list))
        self.assertEqual(data, data2)

    def test_fetch_airport(self):
        api = API()
        data = API.fetch_data('data/airport', {'ids': 'KJFK', 'format': 'json'})
        data2 = api.get_airport_data('KJFK')
        self.assertIsInstance(data, (dict, list))
        self.assertIsInstance(data2, (dict, list))
        self.assertEqual(data, data2)

    def test_mandatory_fields(self):
        api = API()
        data = api.get_metar_data('KJFK')
        for fieldname in ['metar_id', 'icaoId', 'receiptTime', 'obsTime', 'reportTime', 'temp', 'dewp', 'wdir', 'wspd', 'visib', 'altim', 'lat', 'lon', 'elev', 'lat', 'lon', 'elev', 'prior', 'name', 'rawOb', 'clouds']:
            self.assertIn(fieldname, data)

if __name__ == '__main__':
    unittest.main()