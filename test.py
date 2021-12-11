player = map[player_x][player_y]
    if ch == "w":
        if map[0][1] == "-":
            map[0][1] = "P"
            create_map(map)
        else:
            print("You can't move up")
            os.system("cls")
            create_map(map)
    elif ch == "s":
        if map[2][1] == "-":
            map[2][1] = "P"
            map[1][1] = "-"
            map[2][0] = "-"
            os.system('cls')
            create_map(map)
        else:
            print("You can't move down")
            os.system('cls')
            create_map(map)
    elif ch == "a":
        if map[1][0] == "-":
            map[1][0] = "P"
            map[1][1] = "-"
            map[1][2] = "-"
            os.system('cls')
            create_map(map)
        else:
            print("You can't move left")
            os.system('cls')
            create_map(map)
    elif ch == 'd':
        if map[0][1] == "-":
            player_x = player_x + 1
            create_map(map)
        else:
            print("You can't move up")
            os.system("cls")
            create_map(map)
    elif ch == "esc":
        exit()