from sensor import Sensor, PressureSensor


class Alarm(object):

    def __init__(self):
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._sensor = Sensor()
        self._is_alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()
        if psi_pressure_value < self._low_pressure_threshold \
                or self._high_pressure_threshold < psi_pressure_value:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on


class AlarmRefactored(object):

    def __init__(self, low_pressure_threshold=17, high_pressure_threshold=21):
        self._low_pressure_threshold = low_pressure_threshold
        self._high_pressure_threshold = high_pressure_threshold
        self._sensor = PressureSensor()
        self._is_alarm_on = False

    def check(self):
        psi_pressure_value = self._sensor.get_psi_pressure()
        if psi_pressure_value < self._low_pressure_threshold \
                or self._high_pressure_threshold < psi_pressure_value:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self):
        return self._is_alarm_on
