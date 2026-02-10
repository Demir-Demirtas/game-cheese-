import pyautogui
import time

print("Move your mouse and press Ctrl+C to see coordinates")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Current position: ({x}, {y})", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print(f"\nFinal position: ({x}, {y})")
