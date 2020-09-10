# bt_init
A simple script to automate initialisation of bluetooth modules, designed for USEL LAB.

## Quick Guide
Edit `/dev/ttyUSB0` to the name of your UART device

### Requirement
Library `pyserial` is required. Run `pip3 install pyserial` to install such package

### Usage
Enter the number you want to begin the sequence with, then press enter. Then plug in a new module in the AT Command mode (e.g. holding the button when plugging in for HC06) and press enter.

HC06 would show four consecutive `OK` whereas HC05 would not show any response and requires further confirmation of rename.

Password for HC05 would remain being the defualt `1234` and the password for HC06 would be set to `0000`. All baud rate should be set to 9600 afterwards.
