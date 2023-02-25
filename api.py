#api.py
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

def initialize_battlefield(size_of_board):
    return [[0 for _ in range(size_of_board)] for _ in range(size_of_board)]

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
            if arr[i][j] not in ['H', 'M']:
                arr[i][j] = 0

def update_board(arr: list, row: int, col: int, ships: list) -> None:
    if row < 0 or col < 0 or row > len(arr) or arr > len(arr) or not ships:
        print("error in update_board. Error with Inputs")
        return

def main():

    felid = initialize_battlefield(4)    #initilize feild with boarder of 3

    sub = 3
    battleship = 4
    minisub = 2
    cruiser = 5
    tracker = 3

    all_ships = [minisub, sub, tracker, battleship, cruiser]

    while 1:

        total = sum(row_and_col(feild, ship) for ship in all_ships)
        print_battlefield(feild)
        #print_battlefield_percentages(feild, total)

        print("Enter location as 'number,letter,hit/miss'")
        correct_input = False
        row = -1
        col = -1
        hit_or_miss = None
        while(correct_input == False):

        col = alpha_to_int[(col).upper()]
        row = int(row)-1
        feild[row][col] = hit_or_miss.upper()
        if hit_or_miss.upper() == 'H':
            print("did you sink the ship? answer (y/n) yes or no")

        update_board(feild, row, col, all_ships)
        #print_battlefield_percentages(feild, total)

        
        #print(feild)


#DO FUNCTION FOR WHEN BATTLESHIP GETS HIT NEXT!!!!!


if __name__ == '__main__':
    main()
