gameboard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

global var_1
player_turn = True
gameover = False
turn = 0
scorep1 = 0
scorep2 = 0

def prt_gameboard():
    print(gameboard["7"] + " | " + gameboard["8"] + " | " + gameboard["9"])
    print("---------")
    print(gameboard["4"] + " | " + gameboard["5"] + " | " + gameboard["6"])
    print("---------")
    print(gameboard["1"] + " | " + gameboard["2"] + " | " + gameboard["3"])


def kane_akri_ree():
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")


def player_input():
    global gameover
    if not gameover:
        while True:
            global var_1
            var_1 = input("Pick a spot: ")
            tsek_an_einai_swsto()
    else:
        meta_gameover()


def tsek_an_einai_swsto():
    global var_1
    tsklst = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if var_1 not in tsklst:
        print("Pick a number between 1-9")
        player_input()
    else:
        check_if_box_is_used()


def check_if_box_is_used():
    x = gameboard[str(var_1)]
    if x == "X" or x == "O":
        print("Spot is used!")
        player_input()
    else:
        upd_gameboard()


def upd_gameboard():
    global player_turn
    if player_turn:
        gameboard[str(var_1)] = "X"
    else:
        gameboard[str(var_1)] = "O"
    check_nikiti()
    kane_kinisi()


def kane_kinisi():
    prt_gameboard()
    tsek_gyro()
    player_input()
    check_nikiti()


def des_poios_paizei():
    global player_turn
    global gameover
    if not gameover:
        if player_turn:
            player_turn = False
            print("Player 1 is playing...")
        else:
            player_turn = True
            print("Player 2 is playing...")
    else:
        pass


def check_nikiti():
    check_nikiti_X()
    check_nikiti_Y()


def check_nikiti_X():
    global gameover
    global scorep2
    if gameboard["7"] == gameboard["8"] == gameboard["9"] == "X":
        print("Player 1 WIN")
        scorep2 += 1
        gameover = True
    elif gameboard["4"] == gameboard["5"] == gameboard["6"] == "X":
        print("Player 1 WIN")
        scorep2 += 1
        gameover = True
    elif gameboard["1"] == gameboard["2"] == gameboard["3"] == "X":
        print("Player 1 WIN")
        scorep2 += 1
        gameover = True
    elif gameboard["7"] == gameboard["4"] == gameboard["1"] == "X":
        print("Player 1 WIN")
        scorep2 += 1
        gameover = True
    elif gameboard["8"] == gameboard["5"] == gameboard["2"] == "X":
        print("Player 1 WIN")
        scorep2 += 1
        gameover = True
    elif gameboard["9"] == gameboard["6"] == gameboard["3"] == "X":
        print("Player 1 WIN")
        scorep2 += 1
        gameover = True
    elif gameboard["1"] == gameboard["5"] == gameboard["9"] == "X":
        print("Player 1 WIN")
        scorep2 += 1
        gameover = True
    elif gameboard["7"] == gameboard["5"] == gameboard["3"] == "X":
        print("Player 1 WIN")
        scorep2 += 1
        gameover = True
    else:
        pass


def check_nikiti_Y():
    global gameover
    global scorep1
    if gameboard["7"] == gameboard["8"] == gameboard["9"] == "O":
        print("Player 2 WIN")
        scorep1 += 1
        gameover = True
    elif gameboard["4"] == gameboard["5"] == gameboard["6"] == "O":
        print("Player 2 WIN")
        scorep1 += 1
        gameover = True
    elif gameboard["1"] == gameboard["2"] == gameboard["3"] == "O":
        print("Player 2 WIN")
        scorep1 += 1
        gameover = True
    elif gameboard["7"] == gameboard["4"] == gameboard["1"] == "O":
        print("Player 2 WIN")
        scorep1 += 1
        gameover = True
    elif gameboard["8"] == gameboard["5"] == gameboard["2"] == "O":
        print("Player 2 WIN")
        scorep1 += 1
        gameover = True
    elif gameboard["9"] == gameboard["6"] == gameboard["3"] == "O":
        print("Player 2 WIN")
        scorep1 += 1
        gameover = True
    elif gameboard["1"] == gameboard["5"] == gameboard["9"] == "O":
        print("Player 2 WIN")
        scorep1 += 1
        gameover = True
    elif gameboard["7"] == gameboard["5"] == gameboard["3"] == "O":
        print("Player 2 WIN")
        scorep1 += 1
        gameover = True
    else:
        pass


def meta_gameover():
    global gameover
    global scorep2
    global scorep1
    print("Player 1 - "+ str(scorep2) + " | " + str(scorep1) + " - Player 2")
    print("Thes na pekseis pali?")
    x = input("y/n: ")
    if x == "y":
        newgame()
    elif x == "Y":
        newgame()
    else:
        quit()


def newgame():
    global gameboard
    global gameover
    global player_turn
    global turn
    turn = 0
    gameover = False
    gameboard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
    prt_gameboard()
    player_input()


def tsek_gyro():
    global turn
    global gameover
    turn += 1
    print("TURN:" + str(turn))
    if not turn == 9:
        des_poios_paizei()
    else:
        gameover = True


if player_turn:
    print("Player 1 is starting first!")
else:
    print("Player 2 is starting first!")

kane_kinisi()
