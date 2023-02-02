def sum(a, b, c):
    return a+b+c

def box():
    zero = 'x' if xlst[0] == 1 else('O' if zlst[0] == 1 else 0)
    one = 'x' if xlst[1] == 1 else('O' if zlst[1] == 1 else 1)
    two = 'x' if xlst[2] == 1 else('O' if zlst[2] == 1 else 2)
    three = 'x' if xlst[3] == 1 else('O' if zlst[3] == 1 else 3)
    four = 'x' if xlst[4] == 1 else('O' if zlst[4] == 1 else 4)
    five = 'x' if xlst[5] == 1 else('O' if zlst[5] == 1 else 5)
    six = 'x' if xlst[6] == 1 else('O' if zlst[6] == 1 else 6)
    seven = 'x' if xlst[7] == 1 else('O' if zlst[7] == 1 else 7)
    eight = 'x' if xlst[8] == 1 else('O' if zlst[8] == 1 else 8)

    print(f"{zero} | {one} | {two}")
    print("--|-- |--")
    print(f"{three} | {four} | {five}")
    print("--|-- |--")
    print(f"{six} | {seven} | {eight}")

def chkwin():
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    for win in wins:
        if(sum(xlst[win[0]], xlst[win[1]], xlst[win[2]]) == 3):
            print('x won the game')
            return 1

    for win in wins:
        if(sum(zlst[win[0]], zlst[win[1]], zlst[win[2]]) == 3):
            print('z won the game')
            return 2

    return 3
  
xlst = [0,0,0,0,0,0,0,0,0]
zlst = [0,0,0,0,0,0,0,0,0]
print("Welcome to tic tac toe")
turn = 1

while(True):
    
    box()
    if(turn == 1):
        print("x turn")
        value = int(input("please Enter value 0 to 8:"))
        xlst[value] = 1
    else:
        print("O turn")
        value = int(input("please Enter value 0 to 8:"))
        zlst[value] = 1

    if(chkwin() != 3):
        break
    
    
    
    value = xlst[0] + xlst[1] + xlst[2] + xlst[3] + xlst[4] + xlst[5] + xlst[6] + xlst[7] + xlst[8] +  zlst[0] + zlst[1] + zlst[2] + zlst[3] + zlst[4] + zlst[5] + zlst[6] + zlst[7] + zlst[8]
    if(value == 9):
        print(" ")
        print(" ")
        print("------------------")
        print('|game tied        |')
        print('|both played well |')
        print('|by Ajay Odedara  |')
        print("------------------")
        print(" ")
        print(" ")
        break
    turn = 1 - turn
