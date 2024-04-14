#!/usr/bin/python3

import tkinter as tk
from datetime import datetime

# Create the main window
window = tk.Tk()
window.overrideredirect(True) # Remove title bar
window.attributes('-topmost', True) # Always on top

# Create a label to display the time
label = tk.Label(window, font=("Arial", 48), fg="white", bg="black") 
label.pack()

def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    label.config(text=now)
    label.after(1000, update_clock) # Run every second

# Handle window movement    
def motion(event):
    x, y = event.x_root, event.y_root
    window.geometry(f'+{x}+{y}')

window.bind('<B1-Motion>', motion) 

# Start the clock 
update_clock()
window.mainloop()

# To use it:
 #   Save as floating_clock.
 #  Make executable with chmod +x floating_clock.py
 # Run with ./floating_clock.py

