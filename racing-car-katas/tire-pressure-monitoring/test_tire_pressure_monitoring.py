import unittest
from unittest.mock import patch
from alarm import Alarm, AlarmRefactored


class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    @patch('sensor.Sensor.pop_next_pressure_psi_value')
    def test_check_temperature_too_low(self, mocked_psi_value):
        mocked_psi_value.return_value = 15
        alarm = Alarm()
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    @patch('sensor.Sensor.pop_next_pressure_psi_value')
    def test_check_temperature_too_high(self, mocked_psi_value):
        mocked_psi_value.return_value = 24
        alarm = Alarm()
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    @patch('sensor.Sensor.pop_next_pressure_psi_value')
    def test_check_temperature_in_range(self, mocked_psi_value):
        mocked_psi_value.return_value = 20
        alarm = Alarm()
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)


class AlarmRefactoredTest(unittest.TestCase):

    @patch('sensor.PressureSensor.get_psi_pressure')
    def test_check_temperature_too_low_patched(self, mocked_psi_value):
        mocked_psi_value.return_value = 15
        alarm = AlarmRefactored()
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    @patch('sensor.PressureSensor.get_psi_pressure')
    def test_check_temperature_too_high_patched(self, mocked_psi_value):
        mocked_psi_value.return_value = 24
        alarm = AlarmRefactored()
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    @patch('sensor.PressureSensor.get_psi_pressure')
    def test_check_temperature_in_range_patched(self, mocked_psi_value):
        mocked_psi_value.return_value = 20
        alarm = AlarmRefactored()
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)
