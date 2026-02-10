import pyautogui
import time
from pynput import keyboard

# Define the two locations (x, y coordinates)
location1 = (100, 100)
location2 = (200, 200)
click_delay = 0.1

# Global flag to control clicking
is_running = False

def on_press(key):
    global is_running
    try:
        if key == keyboard.Key.f6:  # Press F6 to toggle
            is_running = not is_running
            print(f"Clicking {'started' if is_running else 'stopped'}")
        elif key == keyboard.Key.f7:  # Press F7 to exit
            print("Exiting script")
            return False
    except AttributeError:
        pass

# Start keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Press F6 to start/stop clicking, F7 to exit")

try:
    while True:
        if is_running:
            pyautogui.click(location1[0], location1[1])
            time.sleep(click_delay)
            pyautogui.click(location2[0], location2[1])
            time.sleep(click_delay)
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Script stopped")
