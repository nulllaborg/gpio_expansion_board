from io_expansion_board_i2c import IoExpansionBoardI2c
import time

io_expansion_board_i2c = IoExpansionBoardI2c(i2c_address=0x24)
io_expansion_board_i2c.pwm_frequency(100)
io_expansion_board_i2c.mode(IoExpansionBoardI2c.PE1,
                            IoExpansionBoardI2c.OUTPUT_PWM_MODE)
io_expansion_board_i2c.mode(IoExpansionBoardI2c.PE2,
                            IoExpansionBoardI2c.OUTPUT_PWM_MODE)

while True:
    io_expansion_board_i2c.duty(IoExpansionBoardI2c.PE1, 50)
    io_expansion_board_i2c.duty(IoExpansionBoardI2c.PE2, 25)
    time.sleep(1)

    io_expansion_board_i2c.duty(IoExpansionBoardI2c.PE1, 25)
    io_expansion_board_i2c.duty(IoExpansionBoardI2c.PE2, 50)
    time.sleep(1)
