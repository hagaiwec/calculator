import tkinter as tk


EMPTY_ENTRY_TEXT = "insert caculation here"


root = tk.Tk()
root.title("Pyculator!")

input_screen = tk.Entry(root, width=50)
buttons = tk.Frame(root)

def clear_input():
    input_screen.delete(0, tk.END)
    input_screen.insert(tk.END, EMPTY_ENTRY_TEXT)
seven_button = tk.Button(text="7", command=None, height=3, width=10).grid(row=1,column=0)
eight_button = tk.Button(text="8", command=None, height=3, width=10).grid(row=1,column=1)
nine_button = tk.Button(text="9", command=None, height=3, width=10).grid(row=1,column=2)
del_button = tk.Button(text="DEL", command=None, height=3, width=10).grid(row=1,column=3)
ac_button = tk.Button(text="AC", command=None, height=3, width=10).grid(row=1,column=4)

four_button = tk.Button(text="4", command=None, height=3, width=10).grid(row=2,column=0)
five_button = tk.Button(text="5", command=None, height=3, width=10).grid(row=2,column=1)
six_button = tk.Button(text="6", command=None, height=3, width=10).grid(row=2,column=2)
mult_button = tk.Button(text="\u00d7", command=None, height=3, width=10).grid(row=2,column=3)
div_button = tk.Button(text="\u00f7", command=None, height=3, width=10).grid(row=2,column=4)

one_button = tk.Button(text="1", command=None, height=3, width=10).grid(row=3,column=0)
two_button = tk.Button(text="2", command=None, height=3, width=10).grid(row=3,column=1)
three_button = tk.Button(text="3", command=None, height=3, width=10).grid(row=3,column=2)
plus_button = tk.Button(text="+", command=None, height=3, width=10).grid(row=3,column=3)
minus_button = tk.Button(text="−", command=None, height=3, width=10).grid(row=3,column=4)

zero_button = tk.Button(text="0", command=None, height=3, width=10).grid(row=4,column=0)
dec_button = tk.Button(text=".", command=None, height=3, width=10).grid(row=4,column=1)
exp_button = tk.Button(text="EXP", command=None, height=3, width=10).grid(row=4,column=2)
ans_button = tk.Button(text="ANS", command=None, height=3, width=10).grid(row=4,column=3)
eq_button = tk.Button(text="EQ", command=None, height=3, width=10).grid(row=4,column=4)

input_screen.grid(row=0, columnspan=5)

root.mainloop()
