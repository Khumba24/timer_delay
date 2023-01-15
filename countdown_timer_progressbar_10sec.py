import time
import sys
import tkinter as tk
from tkinter import ttk

toggle = True

def progressbar(value):

    try:
        progress_bar['value'] = value*10
        progress_bar.update_idletasks()

    except:
        pass

def countdown(t):
    while t>0:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        timer_label.configure(text=timeformat)
        timer_label.update()
        progressbar(t)
        time.sleep(1)
        t -= 1
    
        if toggle == False:
            t = 0
        elif t == 0:
            win.destroy()
            
def stop_delay():

    global toggle
    toggle = False

    win.destroy()
    

if __name__ == "__main__":

    win = tk.Tk()
    win.title('Delay')
    win.geometry('220x120')
    win.resizable(False, False)
    
    
    timer_label = tk.Label(win,text='00:00',font='Helvetica', fg='blue')
    timer_label.place(relx=0.5, rely=0.25, anchor='center')
   
    end_timer = ttk.Button(win, width=15,  text='OK', command=stop_delay)
    end_timer.place(relx=0.5, rely=0.5, anchor='center')

    progress_bar = ttk.Progressbar(win, orient='horizontal', length=100, mode='determinate')
    progress_bar.place(relx=0.5, rely=0.75, anchor='center')
    
    countdown(10)

    win.mainloop()
