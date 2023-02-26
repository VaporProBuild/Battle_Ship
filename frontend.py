import tkinter as tk
import copy
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

def button_callback(button, label_text, arr, copies):
	copies.append(copy.deepcopy(arr))	#create a copy of the old map
	arr[button.row][button.col] = 'X'
	label_text.set(f"Button at row {button.row}, column {button.col} was clicked")
	button.set_text(f"{arr[button.row][button.col]}")
	emptyBoard(arr)
	xrow_and_col(arr, ships)
	button.update_all_texts(" ", arr)
	for all in copies:
		print(all)
		print()


def create_button_callback(button, label_text, arr, copies):
    def callback():
        button_callback(button, label_text, arr, copies)
    return callback

def create_table(root, sob, arr, copies):
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
				button.config(command=create_button_callback(button, label_text, arr, copies), width=3, height=3)
				button.grid(row=row, column=col)
	
	# Update the frame to get its current size
	root.update()
	label = tk.Label(root, textvariable=label_text, width = root.winfo_width(), height = 2, anchor="center", justify="center")
	label.place(relx=0.5, rely=1.0, anchor="s", y=-55)

	btn_frame = tk.Frame(root, width=200, height = 2)
	btn_frame.place(relx=0.5, rely=1.0, anchor="s", y=-35)

	hit_btn = tk.Button(btn_frame, text="HIT!", width = 10, height = 1, anchor="center", justify="center")
	hit_btn.pack(side=tk.LEFT, padx=10)

	sunk_btn = tk.Button(btn_frame, text="SUNK!", width = 10, height = 1, anchor="center", justify="center")
	sunk_btn.pack(side=tk.LEFT, padx=10)

	undo_btn = tk.Button(root, command=create_undo(root, arr, copies), text="UNDO", width = 10, height = 1, anchor="center", justify="center")
	undo_btn.place(relx=0.5, rely=1.0, anchor="s", y=-5)

def create_undo(root, arr, copies):
    def callback():
        undo(root, arr, copies)
    return callback

def undo(master, arr, copies):
	print("TEst", len(copies))

	if len(copies) == 0 or copies == []:
		print("you are at the beginning!!")
		return
	
	#if user hasnt changed since last time only pop once
	#print(copies)
	prev = copies.pop().copy()
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			arr[i][j] = prev[i][j]

	
	tb = TableButton(master, 0, 0)
	tb.button_list.pop()
	tb.update_all_texts("", arr)

	for all in copies:
		print(all)
		print()


def main():
	all_battlefields = []

	felid = initialize_battlefield(sob)
	total = xrow_and_col(felid, ships)
	
	root = tk.Tk()
	height = 23 + sob * 62 + 90	#topbar + num_squares * length_squares + Bottom extension
	width = 23 + sob * 70
	root.geometry(f"{width}x{height}")

	create_table(root, sob, felid, all_battlefields)

	root.mainloop()

if __name__ == '__main__':
	main()

#TODO Add sink functionality!
#TODO Add comments to code
#TODO Add Hit functionality and colors.