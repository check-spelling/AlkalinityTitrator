# Program constants and strings
ROUTINE_OPTIONS = {
    1: 'Run titration',
    2: 'Calibrate sensors',
    3: 'Update settings',
    4: 'Test',
    5: 'Exit'
}
SENSOR_OPTIONS = {
    1: 'pH',
    2: 'Temperature'
}
VALID_INPUT_WARNING = 'Please enter a valid input'
KEY_0 = 10
KEY_1 = 11
KEY_2 = 12
KEY_3 = 13
KEY_4 = 14
KEY_5 = 15
KEY_6 = 16
KEY_7 = 17
KEY_8 = 18
KEY_9 = 19
# for pH calibration constants
calibrated_pH = {
    'measured': [None, None],
    'actual': [None, None],
    'slope': None
}
# temp
calibrated_ref_resistor_value = 4300.0
nominal_resistance = 1000.0
# titration routine
TARGET_TEMP = 0.0  # degrees C
TARGET_PH = 3.0
TEMPERATURE_ACCURACY = 0.5
STABILIZATION_CONSTANT = 0.1  # how much the pH is allowed to change between measurements to ensure the value is stable
PH_ACCURACY = 0.05
SLEEP_TIME = 1
INCREMENT_AMOUNT = 0.5

# TESTING
test_pH_vals = [[7.0, 6.8, 6.5, 6.4, 6.0, 5.4, 5.2, 5.1, 5.1, 5.0, 5.0, 5.0],
                [5.0, 4.5, 4.4, 4.1, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9, 3.9],
                [3.9, 3.8, 3.7, 3.6, 3.5, 3.5, 3.5, 3.5, 3.5]]
hcl_call_iter = 0
pH_call_iter = -1

