import time
import json
import pyautogui
from pynput.keyboard import Controller as KeyboardController

# Load recorded events
with open("events.json", "r") as f:
    events = json.load(f)

keyboard = KeyboardController()
start_time = events[0]["time"]

for event in events:
    if event["type"] == "key_press":
        keyboard.press(event["key"])
        keyboard.release(event["key"])
    
    elif event["type"] == "mouse_click":
        if event["pressed"]:
            pyautogui.mouseDown(event["x"], event["y"], button=event["button"])
        else:
            pyautogui.mouseUp(event["x"], event["y"], button=event["button"])

    elif event["type"] == "mouse_move":
        pyautogui.moveTo(event["x"], event["y"], 0)

print("Playback complete!")
