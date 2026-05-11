class Thermometer:
    def __init__(self, celsius):
        self.__celsius = celsius
        self.__history = [celsius]
    def get_celsius(self):
        return self.__celsius
    def set_celsius(self, value):
        if value < -273.15:
            print("Ошибка: ниже абсолютного нуля")
            return
        self.__celsius = value
        self.__history.append(value)
    def get_fahrenheit(self):
        return self.__celsius * 9/5 + 32
    def get_history(self):
        return self.__history.copy()