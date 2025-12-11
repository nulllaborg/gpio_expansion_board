# I/O Expansion Module

## Product Image

<img src="./pictures/i2c_gpio_expansion_board.jpg" title="" alt="Product Image" data-align="center">

## Introduction

This NULLLAB I/O Expansion Module solves the common issue of scarce on-board ADC, IO, I2C, or PWM ports. It provides vital expansion: 4 I2C interfaces and 8 highly flexible GPIO ports, ensuring ample connectivity for complex projects.

The 8 GPIO ports are individually software-configurable as ADC, Digital I/O, or PWM Output (1 to 10 kHz). The PWM mode directly supports driving servos. Configuration is managed via the I2C interface (default address: 0x24), which is customizable using solder pads on the rear of the board.

The chip model of this module is the CH32V003 microcontroller. Using this module does not require programming the CH32V003; it is only necessary to communicate with other devices via the I2C interface. For detailed communication methods, please refer to the example program.

### Extended Pins

| Pins Types | Quantity |
| ---------- | -------- |
| I2C        | 4        |
| GPIO       | 8        |

### GPIO Pin Functions

| GPIO Pin | Configurable Functions                                  |
| -------- | ------------------------------------------------------- |
| E0       | ADC Input, Digital Input, Digital Output                |
| E1       | ADC Input, Digital Input, Digital Output, or PWM Output |
| E2       | ADC Input, Digital Input, Digital Output, or PWM Output |
| E3       | ADC Input, Digital Input, Digital Output                |
| E4       | ADC Input, Digital Input, Digital Output                |
| E5       | ADC Input, Digital Input, Digital Output                |
| E6       | ADC Input, Digital Input, Digital Output                |
| E7       | ADC Input, Digital Input, Digital Output                |

### GPIO Functions Description

| Function       | Description                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| ADC Input      | ADC Mode provides 10-bit resolution (0 to 1023 range) for reading analog values                                                 |
| Digital Input  | Supports Pull-up, Pull-down, or Floating input configurations for reading logic high/low states                                 |
| Digital Output | Allows configuration to output a High or Low logic level                                                                        |
| PWM Output     | Configurable frequency (1Hz to =10kHz). Duty cycle is set with 12-bit resolution (0 to 4095 range). Suitable for driving servos |

## Module Parameter

| Pin Name    | Description           |
| ----------- | --------------------- |
| G           | GND (Ground)          |
| V           | 3~5V Power Supply Pin |
| SDA         | I2C Data Pin          |
| SDL         | I2C Clock Pin         |
| I2C Address | 0x24                  |

### Arduino Libs and Examples

[Download Arduino libs](https://github.com/emakefun-arduino-library/emakefun_gpio_expansion_board/archive/refs/tags/release.zip), including Arduino libs and [examples](https://github.com/emakefun-arduino-library/emakefun_gpio_expansion_board#%E7%A4%BA%E4%BE%8B%E7%A8%8B%E5%BA%8F)

### MicroBit Libs and Examples

<a href="./io_expansion_board_i2c_microbit_micropython" download>Micropython libs and examples</a>

Microbit MakeCode lib link: https://github.com/emakefun-makecode-extensions/emakefun_io_extension_board

### ESP32 MicroPython Examples

<a href="./io_expansion_board_i2c_esp32_micropython" download>Libs and examples</a>


