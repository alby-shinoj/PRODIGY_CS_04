# PRODIGY_CS_04
keylogger

Steps to Run the Keylogger:
Install the required library:
pip install pynput

Run the script:
python keylogger.py

Explanation:
Logging Configuration: The logging.basicConfig function sets up the logging configuration, specifying the filename (keylog.txt), logging level (DEBUG), and format.
on_press Function: This function is called whenever a key is pressed. It logs the key press to the file.
Listener: The Listener from pynput.keyboard listens for key presses and calls the on_press function.
