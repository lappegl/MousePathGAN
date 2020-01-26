# CollectMouseData.py
# Author - Garrett Lappe - garrett.l.lappe@gmail.com
# Simple script to run the CollectorGUI


from CollectorGUI import CollectorGUI
from tkinter import Tk

if __name__ == '__main__':

    root = Tk()
    collector = CollectorGUI(root)
    root.mainloop()
