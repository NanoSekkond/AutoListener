from pynput import keyboard, mouse
from my_modules import Input
from time import sleep

class GlobalListener:
    is_running = False
    input_list = []
    wait = 0
    def __init__(self, max_wait) -> None:
        self.keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_press, on_release=self.on_keyboard_release)
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move, on_click=self.on_mouse_click, on_scroll=self.on_mouse_scroll)
        self.max_wait = max_wait

    def start(self):
        self.is_running = True
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def stop(self):
        self.is_running = False
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

    def on_keyboard_press(self, key):
        if (key == keyboard.Key.esc):
            self.stop()
            return
        self.input_list.append(Input.Input(key, 0))

    def on_keyboard_release(self, key):
        self.input_list.append(Input.Input(key, 1))

    def on_mouse_move(self, x, y):
        if (self.wait == 0):
            self.input_list.append(Input.Input(None, 2, [x, y]))
            self.wait = self.max_wait
        else:
            self.wait -= 1

    def on_mouse_click(self, x, y, button, pressed):
        action = 0 if pressed else 1
        self.input_list.append(Input.Input(button, action, [x, y]))

    def on_mouse_scroll(self, x, y, dx, dy):
        self.input_list.append(Input.Input(None, 2, [x, y], [dx, dy]))