from root import *

# Menu Class
class MenuBS:
    __list=[]

    def getList(self):
        return self.__list

    def __init__(self,
                 root,
                 bg='#050505',
                 fg='white',
                 borderWidth=0,
                 font=('verdana 15'),
                 cursor='hand2',
                 height=2):
        # Create automatic style menu buttons
        try:
            self.root = root
            self.activeFg = 'black'
            self.activeBg = 'white'
            self.bg = bg
            self.fg = fg
            self.borderWidth = borderWidth
            self.font = font
            self.cursor = cursor
            self.height = height
        except:
            return

    def __on_Enter(self, e):
        try:
            e.widget['background'] = self.activeBg
            e.widget['foreground'] = self.activeFg
        except:
            return

    def __on_Leave(self, e):
        try:
            e.widget['background'] = self.bg
            e.widget['foreground'] = self.fg
        except:
            return

    def addElement(self, button):
        try:
            button['bg'] = self.bg
            button['fg'] = self.fg
            button['borderwidth'] = self.borderWidth
            button['font'] = self.font
            button['cursor'] = self.cursor
            button['height'] = self.height
            button.bind("<Enter>", self.__on_Enter)
            button.bind("<Leave>", self.__on_Leave)
            self.__list.append(button)
        except:
            return

    def pack(self):
        try:
            for btn in self.__list:
                btn.pack(side=LEFT, anchor=NW)
        except:
            return

    def unpack(self):
        try:
            for btn in self.__list:
                btn.destroy()
        except:
            return