from io_expansion_board_i2c import IoExpansionBoardI2c
import machine
import time

io_expansion_board_i2c = IoExpansionBoardI2c(i2c=machine.I2C(0, sda=21, scl=22),
                                             i2c_address=0x24)
io_expansion_board_i2c.pwm_frequency = 1000
io_expansion_board_i2c[1].mode = IoExpansionBoardI2c.OUTPUT_PWM_MODE
io_expansion_board_i2c[2].mode = IoExpansionBoardI2c.OUTPUT_PWM_MODE

print('start')

while True:
    io_expansion_board_i2c[1].pwm_duty = 2048
    io_expansion_board_i2c[2].pwm_duty = 4095
    time.sleep(1)

    io_expansion_board_i2c[1].pwm_duty = 4095
    io_expansion_board_i2c[2].pwm_duty = 2048
    time.sleep(1)
