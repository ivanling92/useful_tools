# -*- coding: utf-8 -*-
"""
Peter Pan 3.0
@author: Ivan Ling

Modules needed: Pynput (pip install pynput//)

This program is designed to make Peter sing a song by posting 1000 comments, in 100 comments chunks.
1. Activate program and remember DO NOT PRESS SHIFT
2. Go to peter's post
3. Make sure cursor is in comment box
4. Press Shift. 
5. Wait and repeat until FB disables comment. 
"""

from pynput.keyboard import Key, Controller, Listener
import time

keyboard = Controller()
key = Key.enter

def activate():
    for i in range(100):
        keyboard.press('h')
        keyboard.release('h')
        time.sleep(0.1)
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(0.1) #To beat the FB auto spam detection

def on_press(key):
    print('{0} pressed'.format(key))
    if key == Key.shift:
        activate()

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()