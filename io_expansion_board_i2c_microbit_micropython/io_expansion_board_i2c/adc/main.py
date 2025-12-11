from io_expansion_board_i2c import IoExpansionBoardI2c

io_expansion_board_i2c = IoExpansionBoardI2c(i2c_address=0x24)
io_expansion_board_i2c.mode(IoExpansionBoardI2c.PE1,
                            IoExpansionBoardI2c.ADC_MODE)

while True:
    print(io_expansion_board_i2c.adc_value(IoExpansionBoardI2c.PE1))
