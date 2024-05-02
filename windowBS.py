from tkinter import *

# Create window class
class WindowBS:
    def __init__(self, stateRoot, iconRoot, titleRoot, bgRoot):
        self.root = Tk()
        self.root.state(stateRoot)
        self.root.wm_iconbitmap(iconRoot)
        self.root.title(titleRoot)
        self.root['bg'] = bgRoot

    def getRoot(self):
        return self.root