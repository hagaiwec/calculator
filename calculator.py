import tkinter as tk


EMPTY_ENTRY_TEXT = "insert caculation here"
BUTTONS_DIMENSIONS = {"rows": 4, "cols": 5}
BUTTONS_LABELS = ["7", "8", "9", "DEL", "AC",
                  "4", "5", "6", "÷", "×",
                  "1", "2", "3", "+", "−",
                  "0", ".", "EXP", "Ans", "="]


def clear_input():
    input_screen.delete(0, tk.END)


def add_to_input(btn_label):
    input_screen.insert(tk.END, btn_label)


def delete_from_input():
    if input_screen.get()[-3:] == "Ans":
        new_input = input_screen.get()[:-3]
        input_screen.delete(0, tk.END)
        input_screen.insert(0, new_input)
    else:
        new_input = input_screen.get()[:-1]
        input_screen.delete(0, tk.END)
        input_screen.insert(0, new_input)


def button_pressed(btn_label):
    print(btn_label)
    if btn_label in "1234567890+−÷×." or btn_label == "Ans":
        add_to_input(btn_label)
        return None
    elif btn_label == "DEL":
        delete_from_input()
        return None
    elif btn_label == "AC":
        clear_input()
        return None
    elif btn_label == "=":
        # result = parse_input(input_screen.get())
        pass
    else:
        pass


root = tk.Tk()
root.geometry("300x500")
root.title("Pyculator!")
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)

input_screen = tk.Entry(root)
input_screen.grid(row=0, sticky=tk.E+tk.W)

result_screen = tk.Entry(root)
result_screen.grid(row=1, sticky=tk.E+tk.W)

buttons = tk.Frame(root)
buttons.grid(row=2, sticky=tk.N+tk.E+tk.W+tk.S)
for r in range(BUTTONS_DIMENSIONS["rows"]):
    buttons.rowconfigure(r, weight=1)
    for c in range(BUTTONS_DIMENSIONS["cols"]):
        buttons.columnconfigure(c, weight=1)
        btn_label = BUTTONS_LABELS[r * BUTTONS_DIMENSIONS["cols"] + c]
        print(btn_label)
        btn = tk.Button(
            buttons, 
            text=btn_label,
            command=lambda btn_label=btn_label: button_pressed(btn_label)
            )
        btn.grid(row=r, column=c, sticky=tk.N+tk.E+tk.W+tk.S)

root.mainloop()