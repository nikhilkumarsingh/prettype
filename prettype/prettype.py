import argparse
import glob
import json
import os

import xerox
from pynput import keyboard

from .gui import FontSelectorGUI

default_key_binding = (keyboard.Key.ctrl, keyboard.Key.space)
default_exit_key = keyboard.Key.esc


class Prettype:
    """
    Master class for prettype which:
     1. listens for a key binding
     2. open font selector GUI when key binding is pressed
     3. Paste the currently selected text in the clipboard with selected font
    """

    def __init__(self, key_binding, exit_key):
        self.fonts_dict = {}
        self.load_fonts()
        self.key_binding = key_binding
        self.exit_key = exit_key
        self.prev_key = None

        print("Starting 🅿🆁🅴🆃🆃🆈🅿🅴 with key-binding \"{}+{}\" and exit-key \"{}\".".format(
            self.key_binding[0],
            self.key_binding[1],
            self.exit_key)
        )
        self.run()

    def run(self):
        """
        pynput keyboard listener
        """
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        """
        Callback function for keyboard listener when a key is pressed
        :param key: pynput.keyboard.Key instance
        :return: True/False. Keyboard listener stops listening when False is returned
        """
        if key == self.exit_key:
            return False

        if (self.prev_key, key) == self.key_binding:
            FontSelectorGUI(on_select=self.paste_formatted_text)

        self.prev_key = key
        return True

    def paste_formatted_text(self, font_type):
        """
        Paste the currently selected text in the clipboard with the input font type
        :param font_type: name of font
        """
        font = self.fonts_dict.get(font_type, 'Serif-Normal')
        text = xerox.paste(xsel=True)
        ftext = ''.join(list(map(lambda ch: font.get(ch, ch), text)))
        xerox.copy(ftext)

    def load_fonts(self):
        """
        Utility function to load all available fonts in a dictionary
        """
        font_paths = glob.glob(os.path.join(os.path.dirname(__file__), 'fonts/*.json'))
        for font_path in font_paths:
            font_name = font_path.split('/')[-1].split('.')[0]
            with open(font_path, 'r') as f:
                self.fonts_dict[font_name] = json.loads(f.read())


def main():
    parser = argparse.ArgumentParser()

    key_binding_help_text = """Set a key binding for triggering prettype font selector. 
    Example: $ prettype -b ctrl space
    """

    exit_key_help_text = """Specify a key which stops the keyboard listener, when pressed. 
    Example: $ prettype -e esc
    """

    parser.add_argument('-b', '--binding', type=str, nargs=2, default=None,
                        metavar=('key1', 'key2'), help=key_binding_help_text)

    parser.add_argument('-e', '--exit_key', type=str, default=None,
                        metavar='key', help=exit_key_help_text)

    args = parser.parse_args()

    key_binding = default_key_binding
    exit_key = default_exit_key

    if args.binding is not None:
        try:
            key1 = getattr(keyboard.Key, args.binding[0])
        except AttributeError:
            key1 = keyboard.KeyCode.from_char(args.binding[0])

        try:
            key2 = getattr(keyboard.Key, args.binding[1])
        except AttributeError:
            key2 = keyboard.KeyCode.from_char(args.binding[1])
        key_binding = (key1, key2)

    if args.exit_key is not None:
        try:
            exit_key = getattr(keyboard.Key, args.exit_key)
        except AttributeError:
            exit_key = keyboard.KeyCode.from_char(args.exit_key)

    Prettype(key_binding, exit_key)


if __name__ == '__main__':
    main()
