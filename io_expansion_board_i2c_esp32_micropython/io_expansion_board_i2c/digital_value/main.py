from io_expansion_board_i2c import IoExpansionBoardI2c
import machine

io_expansion_board_i2c = IoExpansionBoardI2c(i2c=machine.I2C(0, sda=21, scl=22),
                                             i2c_address=0x24)
io_expansion_board_i2c[0].mode = IoExpansionBoardI2c.OUTPUT_DIGITAL_MODE
io_expansion_board_i2c[1].mode = IoExpansionBoardI2c.INPUT_PULL_UP_MODE

while True:
    print('digital value:', io_expansion_board_i2c[1].value)
    io_expansion_board_i2c[0].value = io_expansion_board_i2c[1].value
