import random
from abc import ABC, abstractmethod


class Sensor(object):
    # The reading of the pressure value from the sensor is simulated in this implementation.
    # Because the focus of the exercise is on the other class.

    _OFFSET = 16

    def pop_next_pressure_psi_value(self):
        pressure_telemetry_value = self.sample_pressure()
        return Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def sample_pressure():
        # placeholder implementation that simulate a real sensor in a real tire
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value


class SensorInterface(ABC):

    @abstractmethod
    def get_psi_pressure(self):
        pass


class PressureSensor(SensorInterface):

    def __init__(self):
        self.sensor = Sensor()

    def get_psi_pressure(self):
        return self.sensor.pop_next_pressure_psi_value()
