from pynput import keyboard, mouse
from time import sleep

class GlobalReplay:
    def __init__(self, inputs) -> None:
        self.k_controller = keyboard.Controller()
        self.m_controller = mouse.Controller()
        self.inputs = inputs
    
    def start(self):
        i = 0
        while (i < len(self.inputs)):
            self.execute(self.inputs[i])
            sleep(0.001)
            if (self.inputs[i].key == mouse.Button.left and self.inputs[i].pressed == 1 and not self.is_next_click(i)):
                sleep(1)
            i += 1

    def execute(self, input):
        if (input.position == None):
            if (input.pressed == 0):
                self.k_controller.press(input.key)
            else:
                self.k_controller.release(input.key)
        else:
            self.m_controller.position = (input.position[0], input.position[1])
            if (input.delta == None):
                if (input.pressed == 0):
                    self.m_controller.press(input.key)
                elif (input.pressed == 1):
                    self.m_controller.release(input.key)
            else:
                self.m_controller.scroll(input.delta[0], input.delta[1])
    
    def is_next_click(self, i):
        if (i + 1 < len(self.inputs)):
            next_input = self.inputs[i + 1]
            return next_input.key == mouse.Button.left and next_input.pressed == 0
        return False
        