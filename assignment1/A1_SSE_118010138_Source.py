import random

# create a puzzleList which includes all the puzzles
puzzleList = ['1', '2', '3', '4', '5', '6', '7', '8', '_']

#create the game template
game = '''
%s %s %s
%s %s %s
%s %s %s
''' % (puzzleList[0], puzzleList[1], puzzleList[2], puzzleList[3], puzzleList[4], puzzleList[5], puzzleList[6], puzzleList[7],puzzleList[8])

#The end of the game form
win = '''
1 2 3
4 5 6
7 8 _
'''

#the condition of the game
condition = True

#the game ends and a new game begins
def greetings():
    print('Welcome to 8-puzzle game, ……… ')
    input('Press any key to begin > ')

#start scrambling before the game by random
def randomPermutation():
    global game
    for i in range(1000):
        if game.find('_') == 1:
            list1 = ['u', 'l']
            moveMent(random.choice(list1))
        if game.find('_') == 3:
            list2 = ['u', 'l', 'r']
            moveMent(random.choice(list2))
        if game.find('_') == 5:
            list3 = ['u', 'r']
            moveMent(random.choice(list3))
        if game.find('_') == 7:
            list4 = ['d', 'u', 'l']
            moveMent(random.choice(list4))
        if game.find('_') == 9:
            list5 = ['u', 'd', 'l', 'r']
            moveMent(random.choice(list5))
        if game.find('_') == 11:
            list6 = ['d', 'u', 'r']
            moveMent(random.choice(list6))
        if game.find('_') == 13:
            list7 = ['d', 'l']
            moveMent(random.choice(list7))
        if game.find('_') == 15:
            list8 = ['d', 'l', 'r']
            moveMent(random.choice(list8))
        if game.find('_') == 17:
            list9 = ['d', 'r']
            moveMent(random.choice(list9))

#tell the player the rule of the game
def gameRule():
    print('''
If you want to move left,you should input "l"'
If you want to move right,you should input "r"
If you want to move down,you should input "d"
If you want to move up,you should input "u"            
          ''')

#replace "_" to " " to show the game to the player and then replace " " back to "_" to operate
def replaceProcess():
    global game
    blank = game.find('_')
    game = game.replace('_', ' ')
    print(game)
    temporaryList = []
    for i in game:
        temporaryList.append(i)
    temporaryList[blank] = '_'
    game = ''.join(temporaryList)

#error information
def error():
    print('Please input a correct direction')

#create the moveMent function corresponding to each movement
def moveMent(move):
    #use the global variable game in the function
    global game
    #move right
    if move == 'r':
        number1 = game[game.find('_') - 2]
        game = game.replace('_','*')
        game = game.replace(number1,'_')
        game = game.replace('*',number1)
    #move left
    if move == 'l':
        number2 = game[game.find('_') + 2]
        game = game.replace('_','*')
        game = game.replace(number2,'_')
        game = game.replace('*',number2)
    #move up
    if move == 'u':
        number3 = game[game.find('_') + 6]
        game = game.replace('_', '*')
        game = game.replace(number3,'_')
        game = game.replace('*',number3)
    #move down
    if move == 'd':
        number4 = game[game.find('_') - 6]
        game = game.replace('_', '*')
        game = game.replace(number4,'_')
        game = game.replace('*',number4)

#the function of beginning the game
def gameProcsss():
    global game
    #the number of the total steps of the game
    sum = 0
    while True:
        replaceProcess()
        #the blank at position1
        while game.find('_') == 1:
            move = input('Input sliding direction(left or up)')
            if move == 'l' or move == 'u':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        # the blank at position2
        while game.find('_') == 3:
            move = input('Input sliding direction(left or up or right)')
            if move == 'l' or move == 'u'or move == 'r':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        # the blank at position3
        while game.find('_') == 5:
            move = input('Input sliding direction(up or right)')
            if move == 'u' or move == 'r':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        # the blank at position4
        while game.find('_') == 7:
            move = input('Input sliding direction(left or up or down)')
            if move == 'l' or move == 'u' or move == 'd':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        # the blank at position5
        while game.find('_') == 9:
            move = input('Input sliding direction(left or up or right or down)')
            if move == 'l' or move == 'u' or move == 'r' or move == 'd':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        # the blank at position6
        while game.find('_') == 11:
            move = input('Input sliding direction(down or up or right)')
            if move == 'd'or move == 'u' or move == 'r':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        # the blank at position7
        while game.find('_') == 13:
            move = input('Input sliding direction(left or down)')
            if move == 'l' or move == 'd':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        # the blank at position8
        while game.find('_') == 15:
            move = input('Input sliding direction(left or down or right)')
            if move == 'l' or move == 'd' or move == 'r':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        # the blank at position9
        while game.find('_') == 17:
            move = input('Input sliding direction(down or right)')
            if move == 'd' or move == 'r':
                # the number of the total steps of the game increases
                sum += 1
                break
            error()
        #use "moveMent" function
        moveMent(move)
        #judge whether the game is over
        if game == win:
            replaceProcess()
            print('Congratulations!  You solved the puzzle in %d moves! '%(sum))
            break

#judge whether the player want to play again or not
def gameAgain():
    global condition
    newGame = input('Do you want to start a new game (Y/N)?')
    if newGame != 'Y':
        condition = None

#the whole process of the game
while condition:
    greetings()
    randomPermutation()
    gameRule()
    gameProcsss()
    gameAgain()






































