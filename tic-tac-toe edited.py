from random import randrange

//todo: دیسپلی 

def display_board(board):
    print("+-------" * 3,"+", sep="") #saakht balaye jaadval 
    for row in range(3): 
        print("|       " * 3,"|", sep="") #saakht row separator 
        for col in range(3): #print the cell value 
            print("|   " + str(board[row][col]) + "   ", end="") #end ejaze mide barname toye hamun row edame bde va be line badi nare!! 
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

//todo: دریافت ورودی از یوزر 

def enter_move(board): 
    ok = False #Ensure it enters the validation loop ,  It starts as False to ensure the loop executes at least once
    while not ok : #unless it iterates through a loop 
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
        if not ok : 
            print("bad move! repeat your input.")
            continue #proceed to the next iteration 
        move = int(move) - 1 #cells number from 0 to 8 (zero-based index)
        row = move // 3 
        col = move % 3
        sign = board[row][col] #Retrieves the current content of the selected square on the board 
        ok = sign not in ['O','X'] #Checks if the square is not already occupied by 'O' or 'X'
        if not ok: 
            print("field already occupied. repeat your input!")
            continue 
    board[row][col] = 'O' # set 'O' at the selected square

//todo: in python we can change the variables values multiple times through the loop. 


//todo: تهیه لیستی از بورد های خالی 

def make_list_of_free_fields(board):
        free = []
        for row in range(3): # iterate through rows
            for col in range(3): # iterate through columns
                if board[row][col] not in ['O','X']: # is the cell free?
                    free.append((row,col)) # yes, it is - append new tuple to the list
        return free

//todo بررسی برنده شدن به تفکیک کاربر یا کامپیوتر

def victory_for(board,sgn): #checks for a victory condition on a 3x3 tic-tac-toe board for a specific symbol sgn ('X' or 'O')
    if sgn == "X":	# are we looking for X?
        who = 'me'	# yes - it's computer's side
    elif sgn == "O": # ... or for O?
        who = 'you'	# yes - it's our side
    else:
        who = None	# we should not fall here!
    cross1 = cross2 = True  # for diagonals #whether all elements in the main //todo: diagonals (cross1) and anti-diagonals (cross2) are equal to sgn. دایاگنال قطر ماتریس می باشد. 
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
            return who
        if board[rc][rc] != sgn: # check 1st diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal //todo: the anti-digonal formula is: board[rc][2 - rc]
            cross2 = False
    if cross1 or cross2:
        return who
    return None







    






        





