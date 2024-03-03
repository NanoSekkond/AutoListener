class Input:

    key = None
    pressed = None
    position = None

    def __init__(self, key, pressed, position = None, delta = None) -> None:
        self.key = key
        self.pressed = pressed
        self.position = position
        self.delta = delta

    def __str__(self):
        return str(self.key) + ", " + str(self.pressed) + ", " + str(self.position) + ", " + str(self.delta)
