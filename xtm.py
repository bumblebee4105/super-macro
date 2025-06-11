from pynput import keyboard, mouse
import time
import json

events = []

# Keyboard event handlers
def on_press(key):
    try:
        events.append({"type": "key_press", "key": key.char, "time": time.time()})
    except AttributeError:
        events.append({"type": "key_press", "key": str(key), "time": time.time()})

def on_release(key):
    if key == keyboard.Key.esc:  # Stop recording when ESC is pressed
        with open("events.json", "w") as f:
            json.dump(events, f, indent=4)
        return False

# Mouse event handlers
def on_click(x, y, button, pressed):
    events.append({
        "type": "mouse_click",
        "x": x,
        "y": y,
        "button": str(button).split(".")[1],
        "pressed": pressed,
        "time": time.time()
    })

def on_move(x, y):
    events.append({
        "type": "mouse_move",
        "x": x,
        "y": y,
        "time": time.time()
    })

# Start listeners
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
mouse_listener = mouse.Listener(on_click=on_click, on_move=on_move)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()
