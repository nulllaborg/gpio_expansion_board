from microbit import i2c
import struct


class IoExpansionBoardI2c:
    NONE_MODE: int = 0,
    INPUT_PULL_UP_MODE: int = 1 << 0
    INPUT_PULL_DOWN_MODE: int = 1 << 1
    INPUT_FLOATING_MODE: int = 1 << 2
    OUTPUT_DIGITAL_MODE: int = 1 << 3
    ADC_MODE: int = 1 << 4
    OUTPUT_PWM_MODE: int = 1 << 5

    PE0: int = 0
    PE1: int = 1
    PE2: int = 2
    PE3: int = 3
    PE4: int = 4
    PE5: int = 5
    PE6: int = 6
    PE7: int = 7

    _ADDRESS_VERSION: int = 0x00
    _ADDRESS_IO_MODE: int = 0x01
    _ADDRESS_ANALOG_VALUES: int = 0x10
    _ADDRESS_VOLTAGE_VALUES: int = 0x20
    _ADDRESS_RATIO_VOLTAGE: int = 0x30
    _ADDRESS_DIGITAL_VALUES: int = 0x40
    _ADDRESS_PWM_DUTY: int = 0x50
    _ADDRESS_PWM_FREQUENCY: int = 0x60

    def __init__(self, i2c_address=0x24) -> None:
        self._i2c_address = i2c_address

    def mode(self, pin, mode):
        if (mode == self.OUTPUT_PWM_MODE) and (pin != self.PE1 and
                                               pin != self.PE2):
            raise ValueError("PE{} is unsupported pwm mode".format(pin))

        i2c.write(self._i2c_address, bytes([self._ADDRESS_IO_MODE + pin, mode]))

    def write_digital(self, pin, value):
        i2c.write(self._i2c_address,
                  bytes([self._ADDRESS_DIGITAL_VALUES + pin, value]))

    def read_digital(self, pin):
        i2c.write(self._i2c_address,
                  bytes([self._ADDRESS_DIGITAL_VALUES + pin]))
        return i2c.read(self._i2c_address, 1)[0]

    def adc_value(self, pin):
        i2c.write(self._i2c_address,
                  bytes([self._ADDRESS_ANALOG_VALUES + (pin << 1)]))
        return struct.unpack("<h", i2c.read(self._i2c_address, 2))[0]

    def pwm_frequency(self, pwm_frequency):
        i2c.write(
            self._i2c_address,
            bytes([self._ADDRESS_PWM_FREQUENCY]) +
            struct.pack("<H", pwm_frequency))

    def pwm_duty(self, pin, duty):
        i2c.write(
            self._i2c_address,
            bytes([self._ADDRESS_PWM_DUTY + (pin << 1)]) +
            struct.pack("<H", int(duty)))

    def servo_angle(self, pin, angle):
        self.pwm_frequency(50)
        self.pwm_duty(pin, ((angle / 90) + 0.5) / 20 * 4095)
        self.mode(pin, self.OUTPUT_PWM_MODE)
