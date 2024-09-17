from pynput.keyboard import Controller

def controlmouse():
    mouse=Controller();
    mouse.position=(10,20)

controlmouse()

def controlkeyboard():
    keyboard=Controller();
    keyboard.type('key')

controlkeyboard()