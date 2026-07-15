from pyfirmata import Arduino, util
import time

PORT = 'COM4'
R, G, B = 9, 10, 11
DUR = 1.0
POT_A = 4
COMMON_ANODE = True
IDLE_SEC = 1.0

board = Arduino(PORT)
it = util.Iterator(board)
it.start()
time.sleep(0.2)

red   = board.get_pin(f'd:{R}:p')
green = board.get_pin(f'd:{G}:p')
blue  = board.get_pin(f'd:{B}:p')
pot   = board.get_pin(f'a:{POT_A}:i')

def write_rgb(r, g, b):
    if COMMON_ANODE:
        red.write(1 - r); green.write(1 - g); blue.write(1 - b)
    else:
        red.write(r); green.write(g); blue.write(b)

def all_off():
    write_rgb(1, 1, 1) if COMMON_ANODE else write_rgb(0, 0, 0)

colors = [
    ("Lavender",       (0.84, 0.40, 0.85)),
    ("Mortar",         (0.37, 0.29, 0.38)),
    ("Nandor",         (0.29, 0.38, 0.31)),
    ("Pine Cone",      (0.38, 0.32, 0.29)),
    ("Trout",          (0.59, 0.31, 0.78)),
    ("Butterfly bush", (0.90, 0.32, 0.65)),
]

try:
    t0 = time.time()
    level = 0.0
    while time.time() - t0 < IDLE_SEC:
        v = pot.read()
        if v is not None:
            level = v
        write_rgb(level, level, level)
        time.sleep(0.01)

    for name, (r, g, b) in colors:
        print(f"Rəng dəyişdi: {name}")
        t_end = time.time() + DUR
        while time.time() < t_end:
            v = pot.read()
            if v is not None:
                level = v
            write_rgb(level * r, level * g, level * b)
            time.sleep(0.01)
finally:
    all_off()
    board.exit()
