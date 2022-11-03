import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    
    @classmethod
    def is_hot_in_pehuajo(self) -> bool:
        """
            True: 
                ->Temperature above 28° Celsius\n
            False:\n 
                ->Temperature less than 28° Celsius\n
                or\n
                ->HTTP Error
        """
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.LAT}&lon={self.LON}&appid={self.API_KEY}&units=metric")
            weather = response.json()
            temperature = weather['main']['temp']
            if temperature > 28: return True
            else: return False
            
        except Exception: 
            return False
            
if __name__ == '__main__':
    g = GeoAPI()
    temperature_above_28 = g.is_hot_in_pehuajo()
    print(temperature_above_28)