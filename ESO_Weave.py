import pynput
import time

mouse = pynput.mouse.Controller()

def on_press(key):
    if not "flag" in globals():
        global flag
        flag = True
    if type(key) != pynput.keyboard.Key:
        if flag:
            if (
                key.char == "1"
                or key.char == "2"
                or key.char == "3"
                or key.char == "4"
                or key.char == "5"
                or key.char == "r"
            ):
                time.sleep(0.20)
                mouse.click(pynput.mouse.Button.left)
                #time.sleep(0.01)
    elif key == pynput.keyboard.Key.tab:
        flag = not flag

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
