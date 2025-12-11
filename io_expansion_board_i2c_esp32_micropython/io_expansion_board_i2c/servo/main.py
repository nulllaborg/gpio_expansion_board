from io_expansion_board_i2c import IoExpansionBoardI2c
import time
import machine

io_expansion_board_i2c = IoExpansionBoardI2c(i2c=machine.I2C(0, sda=21, scl=22),
                                             i2c_address=0x24)
io_expansion_board_i2c.pwm_frequency = 50
io_expansion_board_i2c[1].mode = IoExpansionBoardI2c.OUTPUT_PWM_MODE
io_expansion_board_i2c[2].mode = IoExpansionBoardI2c.OUTPUT_PWM_MODE

while True:
    io_expansion_board_i2c[1].servo_angle = 0
    io_expansion_board_i2c[2].servo_angle = 90
    print('angle:', io_expansion_board_i2c[1].servo_angle, ",",
          io_expansion_board_i2c[2].servo_angle)
    time.sleep(1)

    # print('angle 90')
    io_expansion_board_i2c[1].servo_angle = 90
    io_expansion_board_i2c[2].servo_angle = 0
    print('angle:', io_expansion_board_i2c[1].servo_angle, ",",
          io_expansion_board_i2c[2].servo_angle)
    time.sleep(1)

    io_expansion_board_i2c[1].servo_angle = 180
    io_expansion_board_i2c[2].servo_angle = 180
    print('angle:', io_expansion_board_i2c[1].servo_angle, ",",
          io_expansion_board_i2c[2].servo_angle)
    time.sleep(1)

    io_expansion_board_i2c[1].servo_angle = 90
    io_expansion_board_i2c[2].servo_angle = 90
    print('angle:', io_expansion_board_i2c[1].servo_angle, ",",
          io_expansion_board_i2c[2].servo_angle)
    time.sleep(1)
