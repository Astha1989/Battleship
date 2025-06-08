import random

Rows = 0
Columns = 0
turns = 0

print("Welcome to battleship!")

while (Rows > 9) or (Columns > 9) or (Rows <= 0) or (Columns <= 0):
    Rows = int(input("Please enter the number of rows you want. \n"))
    Columns = int(input("Please enter the number of columns you want. \n"))

def create_grid(Rows, Columns):
    #Creates the 2D Data Grid
    grid = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
            row.append(' ')
        grid.append(row)
    return grid

grid = create_grid(Rows,Columns)

def display_grid(grid, Columns):
    #Prints the labels for the grid
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
    print('  | ' + ' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid):
       print(number + 1, '| ' + ' | '.join(row) + ' |')

display_grid(grid, Columns)

def random_row(grid):
    #Makes a random row integer
    return random.randint(1,len(grid))

def random_col(grid):
    #Makes a random column integer
    return random.randint(1,len(grid[0]))

def update_gridHit(grid, GuessRow, GuessColumn):
    grid[GuessRow-1][GuessColumn-1] = 'O'

def update_gridMiss(grid, GuessRow, GuessColumn):
    grid[GuessRow-1][GuessColumn-1] = 'X'


shipRows=[]
shipCols=[]
for i in range(0, 5):
    shipRows.append(random_row(grid))
    shipCols.append(random_col(grid))

#Testing purposes only, comment out if needed.
print(shipRows)
print(shipCols)

hit=0
while (turns != 10):
    GuessRow = int(input("What row do you guess? \n"))
    GuessColumn = int(input("What column do you guess? \n"))
    found=0


    for i in range(0, 5):
        if (GuessRow == shipRows[i]) and (GuessColumn == shipCols[i]):
            turns += 1
            update_gridHit(grid, GuessRow, GuessColumn)
            display_grid(grid, Columns)
            print("You hit a battleship! Congratulations!")
            found=1
            hit=hit+1
            break

    if hit==5:
        print('You hit all the ships!')
        break
    if found==0:
        if (GuessRow < 1 or GuessRow > Rows) or (GuessColumn < 1 or GuessColumn > Columns):
            #Warning if the guess is out of the board
            print("Sorry, that's not even in the ocean! Please pick a number within your Rows and Columns.")

        elif (grid[GuessRow-1][GuessColumn-1] == "X"):
            #If "X" is there than print that it missed
            print("You guessed that already.")

        else:
            #Updates the grid with an "X" saying that you missed the ship
            turns += 1
            print("You missed the ship.")
            update_gridMiss(grid, GuessRow, GuessColumn)
            display_grid(grid, Columns)

    if (turns >= 10):
        print("Game over! You ran out of tries")
