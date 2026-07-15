from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

red = board.get_pin("d:11:o")
green = board.get_pin("d:12:o")
blue = board.get_pin("d:13:o")

def change_red():
    red.write(0.2)
    green.write(0.7)
    blue.write(1)

def change_green():
    red.write(1)
    green.write(0.2)
    blue.write(1)

def change_blue():
    red.write(1)
    green.write(1)
    blue.write(0.3)

def change_white():
    red.write(0.1)
    green.write(0.1)
    blue.write(0.1)

while True:
    change_red()
    time.sleep(1)
    change_green()
    time.sleep(1)
    change_blue()
    time.sleep(1)
    change_white()
    time.sleep(1)

board.exit()
