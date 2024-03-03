from pynput import keyboard
import sys

class ReplayListener:
    is_running = False
    def __init__(self, global_replay) -> None:
        self.keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_press, on_release=self.on_keyboard_release)
        self.global_replay = global_replay
    
    def start(self):
        self.is_running = True
        self.keyboard_listener.start()

    def stop(self):
        self.is_running = False
        self.keyboard_listener.stop()

    def on_keyboard_press(self, key):
        if (key == keyboard.Key.esc):
            self.stop()
        if key == keyboard.Key.f10:
            print("Your inputs are being replayed...")
            self.global_replay.start()
            print("Done!")
    
    def on_keyboard_release(self, key):
        pass
    