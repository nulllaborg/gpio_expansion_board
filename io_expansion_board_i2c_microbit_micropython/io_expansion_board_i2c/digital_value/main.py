from io_expansion_board_i2c import IoExpansionBoardI2c

io_expansion_board_i2c = IoExpansionBoardI2c(i2c_address=0x24)
io_expansion_board_i2c.mode(IoExpansionBoardI2c.PE0,
                            IoExpansionBoardI2c.OUTPUT_DIGITAL_MODE)
io_expansion_board_i2c.mode(IoExpansionBoardI2c.PE1,
                            IoExpansionBoardI2c.INPUT_PULL_UP_MODE)

while True:
    value = io_expansion_board_i2c.read_digital(IoExpansionBoardI2c.PE1)
    print('digital value:', value)
    io_expansion_board_i2c.write_digital(IoExpansionBoardI2c.PE0, value)
