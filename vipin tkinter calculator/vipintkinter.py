import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget to display numbers
        self.entry = tk.Entry(master, width=25, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("C", 5, 0, columnspan=2)
        self.create_button("AC", 5, 2, columnspan=2)

    def create_button(self, text, row, column, columnspan=1, pady=5):
        button = tk.Button(self.master, text=text, width=5, height=2, pady=pady,
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5)

    def button_click(self, text):
        if text == "C":
            self.entry.delete(-1, tk.END)
        elif text == "AC":
            self.entry.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, text)

# create main window
root = tk.Tk()

# create calculator instance
calculator = Calculator(root)

# run the main event loop
root.mainloop()
