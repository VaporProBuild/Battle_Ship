import tkinter as tk

class TableButton(tk.Button):
    def __init__(self, master, row, col, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.row = row
        self.col = col

def button_callback(button):
    label_text.set(f"Button at row {button.row}, column {button.col} was clicked")

def create_button_callback(button):
    def callback():
        button_callback(button)
    return callback

def create_table(root, rows, cols):
    for row in range(rows):
        for col in range(cols):
            button = TableButton(root, row, col, text=f"({row}, {col})")
            button.config(command=create_button_callback(button))
            button.grid(row=row, column=col)

root = tk.Tk()
label_text = tk.StringVar()
label_text.set("Click a button to see its row and column index")
label = tk.Label(root, textvariable=label_text)
label.grid(row=6, column=0, columnspan=5, padx=5, pady=5, sticky="S")
create_table(root, 5, 5)
root.mainloop()
