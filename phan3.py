import random
import msvcrt
import os

def generate_map(rows, cols):
    map = [['-']*cols for i in range(rows)]  
    map[0][0] = 'P' 
    return map  

def generate_object(map, rows, cols, obj_char):
    while True:  
        x_K = random.randint(0, rows-1)  
        y_K = random.randint(0, cols-1) 
        if map[x_K][y_K] == '-':   
            map[x_K][y_K] = obj_char  
            break                     

def print_map(map, rows, cols):
    print()
    for x in range(rows):
        for y in range(cols):
            print(map[x][y], end=' ')
        print()

def move(map, rows, cols, ch, x_P, y_P):
    x_P_new = x_P
    y_P_new = y_P
    if ch == 'W':
        x_P_new = max(0, x_P-1)
    elif ch == 'S':  
        x_P_new = min(rows-1, x_P+1)
    elif ch == 'A':
        y_P_new = max(0, y_P-1)
    elif ch == 'D':  
        y_P_new = min(cols-1, y_P+1)
    elif ch == 'Q':
        exit()

    value = map[x_P_new][y_P_new]  
    map[x_P][y_P] = '-'           
    map[x_P_new][y_P_new] = 'P'    
    return x_P_new, y_P_new, value

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
map = generate_map(rows, cols)
generate_object(map, rows, cols, 'K')
generate_object(map, rows, cols, 'D')

x_P = 0
y_P = 0
found_key = False

print_map(map, rows, cols)
print("== THE ESCAPE GAME ==\nUSE WASD TO MOVE THE (P)LAYER\nPRESS Q TO QUIT\nTAKE THE (K)EY TO THE (D)OOR TO WIN")

while True:
    ch = msvcrt.getch().decode('utf-8').upper()
    x_P, y_P, value = move(map, rows, cols, ch, x_P, y_P)
    found_key == False
    if found_key == False and value == 'K':
        found_key = True 
        os.system('cls')
        print_map(map, rows, cols)
    elif found_key == False and value == 'D':
        print('YOU LOSE.')
        print('Maybe find the Key first?')
        break

    if found_key and value == 'D':
        os.system('cls')
        print_map(map, rows, cols)
        print('YOU WON!!!')
        break 
    else:          
        print('YOU LOSE.')
        print('Maybe find the Key first?')
    
    os.system('cls')
    print_map(map, rows, cols)