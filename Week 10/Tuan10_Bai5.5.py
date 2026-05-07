class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._c = 0.0
        self.celsius = celsius

    @property
    def celsius(self):
        return self._c
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError()
        self._c = value
    @property
    def fahrenheit(self):
        return self._c * 9/5 + 32
    @fahrenheit.setter
    def fahrenheit(self, value: float):
        c = (value - 32) * 5/9
        if c < -273.15:
            raise ValueError()
        self._c = c