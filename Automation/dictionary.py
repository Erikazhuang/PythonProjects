theBoard = {'TL':' ','TM':' ','TR':' ', 'ML':' ', 'MM': ' ', 'MR':' ','LL':' ','LM':' ','LR':' '}

def printBoard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])


def TicTacToe():
    turn = 'X'

    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')

        move = input()
        theBoard[move]=turn

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    printBoard(theBoard)


#TicTacToe()



#nested dictionary
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBought(guests, item):
    numBought = 0

    for v in guests.values():
        numBought = numBought + v.get(item,0)
    return numBought

def AddNumber(num1, num2):
    return num1 + num2

#count = totalBought(allGuests,'cups')
#print(count)


if __name__ =="__main__":
    import sys
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(AddNumber(num1,num2) )
    print(f'sys argv 0 {sys.argv[0]}')