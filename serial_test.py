import serial
import random

uart_1 = serial.Serial(port='COM4', baudrate=9600, timeout=0.1)
data = 'a'


def read():
    return uart_1.readline()


def write(data_tx):
    uart_1.write(str(data_tx, 'utf-8'))


while True:
    write(data)
    data = read()

    if str(data, 'utf-8') != '':
        print(f"{str(data, 'utf-8')}")
