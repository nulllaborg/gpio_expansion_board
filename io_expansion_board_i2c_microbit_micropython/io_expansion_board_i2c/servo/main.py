from io_expansion_board_i2c import IoExpansionBoardI2c
import time

io_expansion_board_i2c = IoExpansionBoardI2c(i2c_address=0x24)
io_expansion_board_i2c.mode(IoExpansionBoardI2c.PE1,
                            IoExpansionBoardI2c.OUTPUT_PWM_MODE)
io_expansion_board_i2c.mode(IoExpansionBoardI2c.PE2,
                            IoExpansionBoardI2c.OUTPUT_PWM_MODE)

while True:
    io_expansion_board_i2c.servo_angle(IoExpansionBoardI2c.PE1, 0)
    io_expansion_board_i2c.servo_angle(IoExpansionBoardI2c.PE2, 0)
    time.sleep(1)

    io_expansion_board_i2c.servo_angle(IoExpansionBoardI2c.PE1, 90)
    io_expansion_board_i2c.servo_angle(IoExpansionBoardI2c.PE2, 90)
    time.sleep(1)

    io_expansion_board_i2c.servo_angle(IoExpansionBoardI2c.PE1, 180)
    io_expansion_board_i2c.servo_angle(IoExpansionBoardI2c.PE2, 180)
    time.sleep(1)

    io_expansion_board_i2c.servo_angle(IoExpansionBoardI2c.PE1, 90)
    io_expansion_board_i2c.servo_angle(IoExpansionBoardI2c.PE2, 90)
    time.sleep(1)
