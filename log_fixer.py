import os
import logging

def process_keylog(log_file):
    try:
        with open(log_file, "r") as f:
            lines = f.readlines()

        # Join the strings to form words
        words = "".join(lines).split()

        # Replace special key codes with appropriate characters
        for i, word in enumerate(words):
            if word == "Key.space":
                words[i] = " "
            if word == "Key.enter":
                words[i] = "\n"
            if word == "Key.shift_r":
                words[i] = ""
            if word == "Key.esc":
                words[i] == "\n"
            # Add more replacements for other special keys if needed
            # For example: elif word == "Key.enter": words[i] = "\n"

        # Combine the words into a sentence
        sentence = "".join(words)

        return sentence

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    try:
        log_file = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', "keylog.log")
        processed_keylog = process_keylog(log_file)

        if processed_keylog:
            print("Processed Keylog:")
            print(processed_keylog)

    except KeyboardInterrupt:
        logging.info("Keylogger stopped.")
