import tkinter as tk
from api import size_of_board as sob
from api import alpha
from api import all_ships as ships
from api import initialize_battlefield, xrow_and_col, emptyBoard

class TableButton(tk.Button):

	button_list = []

	def __init__(self, master, row, col, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.row = row
		self.col = col
		self.button_list.append(self)

	def set_text(self, text):
		self.configure(text=text)

	def update_all_texts(self, text, arr):
		row = 0
		col = 0
		for btn in self.button_list:
			btn.configure(text=f"{arr[row][col]}")
			col += 1
			if col == sob:
				col = 0
				row += 1

def button_callback(button, label_text, arr):
	arr[button.row][button.col] = 'X'
	label_text.set(f"Button at row {button.row}, column {button.col} was clicked")
	button.set_text(f"{arr[button.row][button.col]}")
	emptyBoard(arr)
	xrow_and_col(arr, ships)
	button.update_all_texts(" ", arr)


def create_button_callback(button, label_text, arr):
    def callback():
        button_callback(button, label_text, arr)
    return callback

def create_table(root, sob, arr):
	label_text = tk.StringVar()
	label_text.set("Click a button to see its row and column index")
	
	for row in range(sob+1):
		for col in range(sob+1):
			if row == 0  and col == 0:
				label = tk.Label(root, text="0")
				label.grid(row=row, column=col)
			elif col == 0:
				label = tk.Label(root, text=f"{row}")
				label.grid(row=row, column=col)
			elif row == 0:
				label = tk.Label(root, text=f"{alpha[col]}")
				label.grid(row=row, column=col)
			else:
				button = TableButton(root, row-1, col-1, text=f"{arr[row-1][col-1]}")
				button.config(command=create_button_callback(button, label_text, arr))
				button.grid(row=row, column=col)

	label = tk.Label(root, textvariable=label_text)
	label.grid(row=sob+2, column=0, columnspan=5, padx=5, pady=5, sticky="S")


def main():
	felid = initialize_battlefield(sob)
	total = xrow_and_col(felid, ships)
	
	root = tk.Tk()

	create_table(root, sob, felid)

	root.mainloop()

if __name__ == '__main__':
	main()