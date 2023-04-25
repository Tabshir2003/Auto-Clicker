import threading
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Set the delay between clicks in seconds (must need to toggle on and off)
delay = 0.001

# Initialize the click state to off
click_state = False

# Define the click function
def click():
    mouse = Controller()
    while True:
        if click_state:
            mouse.click(Button.left)
        time.sleep(delay)

# Start the click function in a separate thread
click_thread = threading.Thread(target=click)
click_thread.start()

# Listen for the "q" key to be pressed and toggle the click state
def on_press(key):
    global click_state
    if key == KeyCode.from_char('t'):
        click_state = not click_state

with Listener(on_press=on_press) as listener:
    listener.join()
