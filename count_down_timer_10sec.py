import time
import sys
import tkinter as tk
from tkinter import ttk

toggle = True

def countdown(t):
    while t>0:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        timer_label.configure(text=timeformat)
        timer_label.update()
        time.sleep(1)
        t -= 1
    
        if toggle == False:
            t = 0
        elif t == 0:
            win.destroy()
    # print('Goodbye!\n\n\n\n\n')


def countdown1(t):
    while t:
        mins, secs = divmod(t, 60)
        hrs, mins = divmod(mins, 60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')

def countdown2(_TIME):
    
    while _TIME > 0:
        m, s = divmod(_TIME, 60)
        h, m = divmod(m, 60)
        print(f"\r{int(h)}".rjust(3,'0'), f"{int(m)}".rjust(2,'0'), 
          f"{s:.3f}".rjust(2,'0'), sep=':', end='')
        _TIME -= 0.06
        time.sleep(0.1)
    else:
        print("\r  Completed !  ")

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
    # timer_label.pack(side='right')
    # timer_label.grid(row=2, column=2, padx=10, pady=5, columnspan=4, sticky='EW')
    timer_label.place(relx=0.5, rely=0.25, anchor='center')
   

    end_timer = ttk.Button(win, width=20,  text='OK', command=stop_delay)
    # end_timer.grid(row=3, column=2, columnspan=4, padx=10, pady=10, sticky='EW')
    end_timer.place(relx=0.5, rely=0.5, anchor='center')
    
    countdown(10)

    win.mainloop()

    

    # countdown(10)
    # countdown2(10)