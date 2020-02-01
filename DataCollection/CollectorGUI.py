# CollectorGUI
# Author - Garrett Lappe - garrett.l.lappe@gmail.com
# Defines custom tkinter GUI for collecting mouse movement data
# Tracks mouse position over time, click position and time, and button location and dimensions for current path.

from tkinter import Button, Label, IntVar
from datetime import datetime
from time import time, sleep
import random
import os


class CollectorGUI:

    def __init__(self, master):
        self.master = master
        self.master.title('Mouse Movement Collection')
        self.master.bind('<Motion>', self.track_movement)
        self.master.bind('<Button-1>', self.track_click)

        self.FRAME_WIDTH = 1000
        self.FRAME_HEIGHT = 500
        master.geometry('{}x{}'.format(self.FRAME_WIDTH, self.FRAME_HEIGHT))  # width x height

        self.start_button = Button(master, text='Start Collection', command=self.spawn_random_button)
        self.start_button.pack()

        self.collected = IntVar(value=0)
        self.collected_total = IntVar(value=0)
        self.num_to_collect = 50

        self.counter = Label(master, textvariable=self.collected)
        self.counter.place(x=10, y=10)
        self.counter_total = Label(master, textvariable=self.collected_total)
        self.counter_total.place(x=10, y=30)

        self.current_button = {}

        # self.button_log = {}
        date = str(datetime.now().date())

        data_dir = 'data\\'
        # make the directory if the folder does not exist
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        filename = data_dir + 'button_log_{}.csv'.format(date)

        print('Output will be written to {}'.format(filename))
        self.button_log_file = open(filename, 'a+')

        self.last_updated = time()

        self.START_TIME = None
        if self.START_TIME is None:
            self.START_TIME = time()
            #print(self.START_TIME)

    # clears the GUI of existing buttons
    def clear_buttons(self):

        buttons = self.master.pack_slaves()
        for b in buttons:
            b.destroy()
        buttons = self.master.place_slaves()
        for b in buttons:
            if isinstance(b, Button):
                b.destroy()
        return

    # creates a new button of random size in a random location on the window
    def spawn_random_button(self):

        self.collected.set(value=(self.collected.get() + 1))  # increment counter
        # CLOSE WINDOW AFTER N BUTTONS PRESSED
        if self.collected.get() > self.num_to_collect:
            self.clear_buttons()
            sleep(.5)
            self.restart()
            return
        self.collected_total.set(value=(self.collected_total.get() + 1))  # increment counter
        self.last_updated = time()
        self.clear_buttons()  # clear previous button
        n = self.collected.get()

        new_button = Button(self.master, text='CLICK ME', command=self.spawn_random_button, bg='red')

        # randomize button dimensions and location
        w = random.randint(15, 100)
        h = random.randint(15, 100)
        x = random.randint(w, self.FRAME_WIDTH - w)
        y = random.randint(w, self.FRAME_HEIGHT - h)

        # log button
        this_button = {
            "x": x,
            "y": y,
            "width": w,
            "height": h
        }

        self.current_button = this_button
        # self.button_log[n] = this_button

        # sleep(.1)  # short break before next button appears
        new_button.place(x=x, y=y, height=h, width=w)

    # when an iteration is complete, spawn a button to restart the collection process
    def restart(self):
        w = 20
        h = 80
        x = random.randint(w, self.FRAME_WIDTH - w)
        y = random.randint(w, self.FRAME_HEIGHT - h)
        self.start_button = Button(self.master, text='Start Collection', command=self.spawn_random_button, bg='blue')
        self.start_button.place(x=x, y=y)
        self.collected.set(0)

    # collects information on movement events (position and time)
    def track_movement(self, event):
        x = event.x_root - self.master.winfo_rootx()
        y = event.y_root - self.master.winfo_rooty()
        # print('({}, {})'.format(x, y), 'button:', self.current_button)
        t = time() - self.last_updated

        if self.collected.get() > 0:
            self.log_action('MOVE', x, y, t, self.current_button)

    # collects information on click events (position and time)
    def track_click(self, event):
        x = event.x_root - self.master.winfo_rootx()
        y = event.y_root - self.master.winfo_rooty()
        t = time() - self.START_TIME

        if self.collected.get() > 0:
            self.log_action('CLICK', x, y, t, self.current_button)

    # writes collected event information to the CSV specified in the initialization of the GUI
    def log_action(self, action, x, y, t, b):
        self.button_log_file.write('{}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(self.collected.get(),
                                                                                 action,
                                                                                 x,
                                                                                 y,
                                                                                 t,
                                                                                 b['x'],
                                                                                 b['y'],
                                                                                 b['width'],
                                                                                 b['height']))
