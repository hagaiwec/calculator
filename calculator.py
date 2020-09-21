import tkinter as tk


EMPTY_ENTRY_TEXT = "insert caculation here"
BUTTONS_DIMENSIONS = {"rows": 4, "cols":5}
BUTTONS_LABELS = ["7", "8", "9", "DEL", "AC",
                  "4", "5", "6", "\u00d7", "\u00f7",
                  "1", "2", "3", "+", "−",
                  "0", ".", "EXP", "ANS", "="]


def clear_input():
    input_screen.delete(0, tk.END)
    input_screen.insert(tk.END, EMPTY_ENTRY_TEXT)


root = tk.Tk()
root.geometry("300x500")
root.title("Pyculator!")
root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)

input_screen = tk.Entry(root)
input_screen.grid(row=0, columnspan=5, sticky=tk.E+tk.W)

buttons = tk.Frame(root)
buttons.grid(row=1, column=1, sticky=tk.N+tk.E+tk.W+tk.S)
for r in range(BUTTONS_DIMENSIONS["rows"]):
    buttons.rowconfigure(r, weight=1)
    for c in range(BUTTONS_DIMENSIONS["cols"]):
        buttons.columnconfigure(c, weight=1)
        btn_label = BUTTONS_LABELS[r * BUTTONS_DIMENSIONS["rows"] + c]
        btn = tk.Button(buttons, text=btn_label)
        btn.grid(row=r, column=c, sticky=tk.N+tk.E+tk.W+tk.S)

root.mainloop()
# seven_button = tk.Button(buttons, text="7", command=None).grid(row=1,column=0, sticky=tk.N+tk.E+tk.W+tk.S)
# eight_button = tk.Button(buttons, text="8", command=None).grid(row=1,column=1, sticky=tk.N+tk.E+tk.W+tk.S)
# nine_button = tk.Button(buttons, text="9", command=None).grid(row=1,column=2, sticky=tk.N+tk.E+tk.W+tk.S)
# del_button = tk.Button(buttons, text="DEL", command=None).grid(row=1,column=3, sticky=tk.N+tk.E+tk.W+tk.S)
# ac_button = tk.Button(buttons, text="AC", command=None).grid(row=1,column=4, sticky=tk.N+tk.E+tk.W+tk.S)

# four_button = tk.Button(buttons, text="4", command=None).grid(row=2,column=0, sticky=tk.N+tk.E+tk.W+tk.S)
# five_button = tk.Button(buttons, text="5", command=None).grid(row=2,column=1, sticky=tk.N+tk.E+tk.W+tk.S)
# six_button = tk.Button(buttons, text="6", command=None).grid(row=2,column=2, sticky=tk.N+tk.E+tk.W+tk.S)
# mult_button = tk.Button(buttons, text="\u00d7", command=None).grid(row=2,column=3, sticky=tk.N+tk.E+tk.W+tk.S)
# div_button = tk.Button(buttons, text="\u00f7", command=None).grid(row=2,column=4, sticky=tk.N+tk.E+tk.W+tk.S)

# one_button = tk.Button(buttons, text="1", command=None).grid(row=3,column=0, sticky=tk.N+tk.E+tk.W+tk.S)
# two_button = tk.Button(buttons, text="2", command=None).grid(row=3,column=1, sticky=tk.N+tk.E+tk.W+tk.S)
# three_button = tk.Button(buttons, text="3", command=None).grid(row=3,column=2, sticky=tk.N+tk.E+tk.W+tk.S)
# plus_button = tk.Button(buttons, text="+", command=None).grid(row=3,column=3, sticky=tk.N+tk.E+tk.W+tk.S)
# minus_button = tk.Button(buttons, text="−", command=None).grid(row=3,column=4, sticky=tk.N+tk.E+tk.W+tk.S)

# zero_button = tk.Button(buttons, text="0", command=None).grid(row=4,column=0, sticky=tk.N+tk.E+tk.W+tk.S)
# dec_button = tk.Button(buttons, text=".", command=None).grid(row=4,column=1, sticky=tk.N+tk.E+tk.W+tk.S)
# exp_button = tk.Button(buttons, text="EXP", command=None).grid(row=4,column=2, sticky=tk.N+tk.E+tk.W+tk.S)
# ans_button = tk.Button(buttons, text="ANS", command=None).grid(row=4,column=3, sticky=tk.N+tk.E+tk.W+tk.S)
# eq_button = tk.Button(buttons, text="EQ", command=None).grid(row=4,column=4, sticky=tk.N+tk.E+tk.W+tk.S)