from tkinter import *
import asyncio
import time
import os
from math import sin,cos
import winsound

#

def run_in_background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped


#

class Notifier:
    def __init__(self,side):
        """
        entry : side == (TOP,BOTTOM)
        """
        assert side == "TOP" or side == "BOTTOM"
        self.windowsOnScreen = []
        self.side = side

    def MoveNotifications(self):
        i = 0
        for roots in self.windowsOnScreen:
            roots.geometry(f"300x100+20+{900-(115*(len(self.windowsOnScreen)-i))}")
            i = i+1

    @run_in_background
    def SendNotification(self, title, description):
        self.MoveNotifications()

        root = Tk()
        root.geometry(f"300x100+20+900")
            #root.geometry(f"300x100+20+{900-(115*(current_index))}")
        root['bg'] = "#2a2a2a"
        root.wm_attributes("-topmost", True)
        root.overrideredirect(True)

        TitleLabel = Label(root, text=str(title), bd = 0, fg = "white", bg = "#2a2a2a", font=("Helvetica", 15))
        ContentLabel = Label(root, text=str(description), bd = 0, fg = "white", bg = "#2a2a2a", font=("Helvetica", 8))

        TitleLabel.pack(pady = 17)
        ContentLabel.pack()

        def fade():
            alpha = root.attributes("-alpha")
            if alpha > 0:
                alpha -= .01
                root.attributes("-alpha", alpha)
                root.after(10, fade)
            else:
                self.windowsOnScreen.remove(root)
                root.quit()      

        self.windowsOnScreen.append(root)
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        root.after(10000,fade)
        root.mainloop()
        pass

class RoundedNotifier:
    def __init__(self,side):
        """
        entry : side == (TOP,BOTTOM)
        """
        assert side == "TOP" or side == "BOTTOM"
        self.windowsOnScreen = []
        self.side = side

    def MoveNotifications(self):
        try:
            i = 0
            for roots in self.windowsOnScreen:
                if self.side == "BOTTOM":
                    roots.geometry(f"300x100+20+{900-(115*(len(self.windowsOnScreen)-i))}")
                else:
                    roots.geometry(f"300x100+20+{20+(115*(len(self.windowsOnScreen)-i))}")
                i = i+1
        except:
            ...

    def create_good_rectangle(self, c, x1, y1, x2, y2, feather, res=5, color='black'):
        points = []

        points += [x1 + feather, y1,
                x2 - feather, y1]

        for i in range(res):
            points += [x2 - feather + sin(i/res*2) * feather,
                    y1 + feather - cos(i/res*2) * feather]

        points += [x2, y1 + feather,
                x2, y2 - feather]

        for i in range(res):
            points += [x2 - feather + cos(i/res*2) * feather,
                    y2 - feather + sin(i/res*2) * feather]

        points += [x2 - feather, y2,
                x1 + feather, y2]

        for i in range(res):
            points += [x1 + feather - sin(i/res*2) * feather,
                    y2 - feather + cos(i/res*2) * feather]

        points += [x1, y2 - feather,
                x1, y1 + feather]

        for i in range(res):
            points += [x1 + feather - cos(i/res*2) * feather,
                    y1 + feather - sin(i/res*2) * feather]
            
        return c.create_polygon(points, fill=color) #?

    @run_in_background
    def SendNotification(self, title, description):
        try:
            self.MoveNotifications()
            root = Tk()

            if self.side == "BOTTOM":
                root.geometry(f"300x100+20+900")
            else:
                root.geometry(f"300x100+20+20")

            root.wm_attributes("-transparentcolor", "green")
            root['bg'] = "green"
            root.wm_attributes("-topmost", True)
            root.overrideredirect(True)

            canvas = Canvas(root, bd=0, highlightthickness=0, relief='ridge')
            canvas["bg"] = "green"
            canvas.pack()

            self.create_good_rectangle(canvas, 0, 0, 300, 100, 25, 100, '#2a2a2a')
            canvas.create_text(149, 30, text= title,fill="white",font=('Helvetica 15 bold'))
            canvas.create_text(149, 60, text= description,fill="white",font=('Helvetica 12 bold'))

            def fade():
                alpha = root.attributes("-alpha")
                if alpha > 0:
                    alpha -= .01
                    root.attributes("-alpha", alpha)
                    root.after(10, fade)
                else:
                    self.windowsOnScreen.remove(root)
                    root.quit()      

            self.windowsOnScreen.append(root)
            
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            root.after(10000,fade)
            root.mainloop()
            pass
        except:
            ...