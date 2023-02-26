#api.py
import copy
"""
API for the classic battleship game. The first block of code is meant for the 
declearation of global constantants that are used in the main testing and or
functions in the program.

the board is defined as list[row][col]

Please refer to the README.md file for instructions on how to run the program.

"""
alpha_to_int = {    #dict to help convert intput to check
	'A' : 0,
	'B' : 1,
	'C' : 2,
	'D' : 3,
	'E' : 4,
	'F' : 5,
	'G' : 6,
	'H' : 7,
	'I' : 8,
	'J' : 9,
	'K' : 10,
	'L' : 11
}

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']

size_of_board = 6

carrier = 5
battleship = 4
cruiser = 3
submarine = 3
destroyer = 2

all_ships = [carrier, battleship, cruiser, submarine, destroyer]

def initialize_battlefield(size_of_board):
    '''
    initializes the board depending on the size given.
    '''
    return [[0 for _ in range(size_of_board)] for _ in range(size_of_board)]

def xrow_and_col(arr, ships_left):
    total = 0
    for ship in ships_left:
        if ship > len(arr):
            print(f"{ship} exceeds limits")
        for var in range(len(arr)):
            for index1 in range(len(arr)):
                index2 = index1 + ship
                if index2>len(arr):
                    break
                col_fits = True
                row_fits = True
                for j in range (index1,index2):
                    if arr[var][j] == 'X':
                        col_fits = False
                        break
                if col_fits:
                    for j in range(index1,index2):
                        arr[var][j] += 1
                        total += 1
                for j in range (index1,index2):
                    if arr[j][var] == 'X':
                        row_fits = False
                        break
                if row_fits:
                    for j in range(index1,index2):
                        arr[j][var] += 1
                        total += 1
    return total

def row_and_col(arr, ship) -> int:
    total = 0
    for col in range(len(arr)):
        for index1 in range(len(arr)):
            index2 = index1 + ship
            if index2>len(arr):
                break
            col_fits = True
            row_fits = True
            for j in range (index1,index2):
                if arr[col][j] == 'M':
                    col_fits = False
            if col_fits == True and arr[col][j] != 'H':
                for j in range(index1,index2):
                    if arr[col][j] != 'H':
                        arr[col][j] += 1
                        total += 1
            for j in range (index1,index2):
                if arr[j][col] == 'M':
                    row_fits = False
            if row_fits and arr[j][col] != 'H':
                for j in range(index1,index2):
                    if arr[j][col] != 'H':
                        arr[j][col] += 1
                        total += 1
    return total

def print_battlefield(arr):

    for i in range(len(arr)):
        if i == 0:
            print(f'    {alpha[i]}', end=' ')    
        else:
            print(f' {alpha[i]}', end=' ')
    print()

    for i in range(len(arr)):
        if i >= 9:
            print(f'{i+1}|', end='')
        else:
            print(f'{i+1} |', end='')
        for j in range(len(arr[i])):
            if j == len(arr[i])-1:  #print the board
                print(arr[i][j], end='')
            else:
                print(arr[i][j], end=' ')
        print("|")
    print()

def emptyBoard(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] not in ['H', 'M', 'X', 'x']:
                arr[i][j] = 0

def update_board(arr: list, row: int, col: int, ships: list) -> None:
    if row < 0 or col < 0 or row > len(arr) or arr > len(arr) or not ships:
        print("error in update_board. Error with Inputs")
        return


def input_board(col, row, felid) -> bool:
    if col not in alpha_to_int.keys() or int(row) < 0:
        print("1.error invalid input!")

    col = alpha_to_int[(col).upper()]
    row = int(row)-1

    if col > size_of_board or row > size_of_board:
        print("2.error invalid input!", col, row,size_of_board)

    felid[row][col] = 'X'

def main():

    felid = initialize_battlefield(size_of_board)    #initilize feild with boarder of 3

    total = 1 #in order to get while loop to begin

    while total > 0:
        total = xrow_and_col(felid, all_ships)
        print_battlefield(felid)
        col, row = input("please enter Col row# > ")
        print(col, row)
        input_board(col, row, felid)

        emptyBoard(felid)

        #update_board(felid, row, col, all_ships)
            #print_battlefield_percentages(felid, total)

            
            #print(felid)


#DO FUNCTION FOR WHEN BATTLESHIP GETS HIT NEXT!!!!!


if __name__ == '__main__':
    main()
