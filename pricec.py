# DO NOT CHANGE ANYTHING UNLESS YOU KNOW WHAT YOU'RE DOING
# price comparator by @cn3z on Discord

# alamak
import tkinter as tk
d1 = 0
p1 = 0
r1 = 0

# gui shit
root = tk.Tk()
root.title("Silly Price Comparator")
root.geometry("320x150")  # size in px
root.resizable(False, False) # nuh uh
root.attributes("-topmost", True) # always on top
root.rowconfigure(0, weight=1) # snap to geometry()
root.columnconfigure(0, weight=1)
frame1 = tk.Frame(root) # frames for gui
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame1.grid(row=0, column=0, sticky='nsew') # grids for frames
frame2.grid(row=0, column=0, sticky='nsew')
frame3.grid(row=0, column=0, sticky='nsew')

# critical functions
def show_frame(frame): # switcharoo!
    frame.tkraise()
def invalidentry(n):
    n.config(bg="red")
    root.after(100, lambda: n.config(bg="white"))
def process_input():
    global d1
    global p1
    global r1
    entrydim = entry2_01.get()
    entryprc = entry2_11.get()
    try:
        d2 = int(entrydim)
        if d2 <= 0: raise ValueError
        p2 = int(entryprc)
        if p2 <= 0: raise ValueError
        r2 = p2/d2
        if r2 > 0 and r1 == 0: # assign to memory (1), (2) is temp
            r1 = r2
            d1 = d2
            p1 = p2
        if r2 > 0: # successful case
            if r1 > r2:
                r1 = r2
                d1 = d2
                p1 = p2
        label2_31.config(text=f"{d2}/{p2} ({r2})")
        label2_21.config(text=f"{d1}/{p1} ({r1})")
    except ValueError:
        invalidentry(entry2_01)
        invalidentry(entry2_11)


# frame 1 content
label1 = tk.Label(frame1, text="Welcome! This program is created to compare prices and shit. For any inquiries, contact @cn3z on Discord. Click the button below to start.",
                  wraplength=320,
                  justify=tk.LEFT
                  )
label1.pack()

button1 = tk.Button(frame1, text="Here!", command=lambda: show_frame(frame2))
button1.pack()

# frame 2 content
label2_00 = tk.Label(frame2, text="Enter the item amount:", justify=tk.LEFT)
label2_10 = tk.Label(frame2, text="Enter the price:", justify=tk.LEFT)
label2_00.grid(row=0, column=0, sticky='w')
label2_10.grid(row=1, column=0, sticky='w')
entry2_01 = tk.Entry(frame2, justify=tk.LEFT)
entry2_11 = tk.Entry(frame2, justify=tk.LEFT)
entry2_01.grid(row=0, column=1, sticky='w')
entry2_11.grid(row=1, column=1, sticky='w')

label2_20 = tk.Label(frame2, text="The most worth: ", justify=tk.LEFT)
label2_30 = tk.Label(frame2, text="Previous one: ", justify=tk.LEFT)
label2_21 = tk.Label(frame2, text="0", justify=tk.LEFT)
label2_31 = tk.Label(frame2, text="0", justify=tk.LEFT)
label2_20.grid(row=2, column=0, sticky='w')
label2_30.grid(row=3, column=0, sticky='w')
label2_21.grid(row=2, column=1, sticky='w')
label2_31.grid(row=3, column=1, sticky='w')

button2_1 = tk.Button(frame2, text="Update", command=process_input)
button2_1.grid(row=4, column=0, sticky='sw')
frame2.rowconfigure(4, weight=1)

show_frame(frame1)
root.mainloop()