import serial
import random

uart_1 = serial.Serial(port='COM4', baudrate=9600, timeout=0.1)


def read():
    return uart_1.readline()


def write(data):
    uart_1.write(bytes(data, 'utf-8'))


while(True):
    output = random.randint(0, 10)
    write(output)
    res = read()

    if(res == output):
        print(f'Success {res} == {output}')

    else:
        print(f'Fail {res} != {output}')
