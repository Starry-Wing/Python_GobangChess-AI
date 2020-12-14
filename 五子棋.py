import turtle as t

def initBoard():
    t.pensize(1)
    t.speed(0)
    for i in range(11):
        t.up()
        t.goto(0,i*20)
        t.seth(0)
        t.down()
        t.forward(200)

    for j in range(11):
        t.up()
        t.goto(j*20,0)
        t.seth(90)
        t.down()
        t.forward(200)

def initChess():
    beginchess=[ [ 0 for i in range(18)] for i in range(18)]
    return beginchess



def blackchess(x,y):
    t.fillcolor('black')
    t.up()
    t.goto(x*20-5,y*20-10)
    t.down()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

def whitechess(x,y):
    t.fillcolor('white')
    t.up()
    t.goto(x*20-5,y*20-10)
    t.down()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

def drawChess(chess):
    for i in range(11):
        for j in range(11):
            if chess[i][j]==1:
                blackchess(i,j)
            if chess[i][j]==2:
                whitechess(i,j)

def AI(chess):
    nowchess = [[0 for i in range(18)] for i in range(18)]
    for i in range(12):
        for j in range(12):
            if i==0 or j==0 or i==11 or j==11:
                nowchess[i][j]=-100
            if i>0 and j>0 and i<11 and j<11:
                if chess[i][j]==1 or chess[i][j]==2:
                    nowchess[i][j]=-100
                    nowchess[i-1][j-1]=nowchess[i-1][j-1]+1
                    nowchess[i][j-1]=nowchess[i][j-1]+1
                    nowchess[i+1][j-1]=nowchess[i+1][j-1]+1
                    nowchess[i-1][j]=nowchess[i-1][j]+1
                    nowchess[i+1][j]=nowchess[i+1][j]+1
                    nowchess[i-1][j+1]=nowchess[i-1][j+1]+1
                    nowchess[i][j+1]=nowchess[i][j+1]+1
                    nowchess[i+1][j+1]=nowchess[i+1][j+1]+1
                nowchess[i][j]=nowchess[i][j]+judgeValue(chess,i,j)


    value=0
    for i in range(12):
        for j in range(12):
            #print('{},{}={}'.format(i, j, nowchess[i][j]))
            if nowchess[i][j]>value:
                value=nowchess[i][j]
    for i in range(12):
        for j in range(12):
            if nowchess[i][j]==value:
                #print(value)
                return i,j


def judgeValue(chess,i,j):
    myvalue=1
    enevalue=0

    if chess[i+1][j]==chess[i+2][j]==2:
        myvalue=myvalue+2
    if chess[i-1][j]==chess[i-2][j]==2:
        myvalue=myvalue+2
    if chess[i][j+1]==chess[i][j+2]==2:
        myvalue=myvalue+2
    if chess[i][j-1]==chess[i][j-2]==2:
        myvalue=myvalue+2
    if chess[i+1][j+1]==chess[i+2][j+2]==2:
        myvalue=myvalue+2
    if chess[i-1][j-1]==chess[i-2][j-2]==2:
        myvalue=myvalue+2
    if chess[i-1][j+1]==chess[i-2][j+2]==2:
        myvalue=myvalue+2
    if chess[i+1][j-1]==chess[i+2][j-2]==2:
        myvalue=myvalue+2
    if chess[i + 1][j] == chess[i + 2][j] ==chess[i+3][j]== 2:
        myvalue = myvalue + 6
    if chess[i - 1][j] == chess[i - 2][j] ==chess[i-3][j]== 2:
        myvalue = myvalue + 6
    if chess[i][j + 1] == chess[i][j + 2] ==chess[i][j+3]== 2:
        myvalue = myvalue + 6
    if chess[i][j - 1] == chess[i][j - 2] == chess[i][j-3]==2:
        myvalue = myvalue + 6
    if chess[i + 1][j+1] == chess[i + 2][j+2] ==chess[i+3][j+3]== 2:
        myvalue = myvalue + 6
    if chess[i - 1][j-1] == chess[i - 2][j-2] ==chess[i-3][j-3]== 2:
        myvalue = myvalue + 6
    if chess[i-1][j + 1] == chess[i-2][j + 2] ==chess[i-3][j+3]== 2:
        myvalue = myvalue + 6
    if chess[i+1][j - 1] == chess[i+2][j - 2] == chess[i+3][j-3]==2:
        myvalue = myvalue + 6


    if chess[i+1][j]==chess[i+2][j]==1:
        enevalue=enevalue+2
    if chess[i-1][j]==chess[i-2][j]==1:
        enevalue=enevalue+2
    if chess[i][j+1]==chess[i][j+2]==1:
        enevalue=enevalue+2
    if chess[i][j-1]==chess[i][j-2]==1:
        enevalue=enevalue+2
    if chess[i+1][j+1]==chess[i+2][j+2]==1:
        enevalue=enevalue+2
    if chess[i-1][j-1]==chess[i-2][j-2]==1:
        enevalue=enevalue+2
    if chess[i-1][j+1]==chess[i-2][j+2]==1:
        enevalue=enevalue+2
    if chess[i+1][j-1]==chess[i+2][j-2]==1:
        enevalue=enevalue+2
    if chess[i + 1][j] == chess[i + 2][j] ==chess[i+3][j]== 1:
        enevalue=enevalue+6
    if chess[i - 1][j] == chess[i - 2][j] ==chess[i-3][j]== 1:
        enevalue=enevalue+6
    if chess[i][j + 1] == chess[i][j + 2] ==chess[i][j+3]== 1:
        enevalue=enevalue+6
    if chess[i][j - 1] == chess[i][j - 2] == chess[i][j-3]==1:
        enevalue=enevalue+6
    if chess[i + 1][j+1] == chess[i + 2][j+2] ==chess[i+3][j+3]== 1:
        enevalue=enevalue+6
    if chess[i - 1][j-1] == chess[i - 2][j-2] ==chess[i-3][j-3]== 1:
        enevalue=enevalue+6
    if chess[i-1][j + 1] == chess[i-2][j + 2] ==chess[i-3][j+3]== 1:
        enevalue=enevalue+6
    if chess[i+1][j - 1] == chess[i+2][j - 2] == chess[i+3][j-3]==1:
        enevalue=enevalue+6

    if chess[i + 1][j] == chess[i + 2][j] == chess[i + 3][j] == chess[i + 4][j] == 1:
        enevalue=enevalue+12
    if chess[i + 1][j] == chess[i + 2][j] == chess[i + 3][j] == chess[i + 4][j] == 2:
        myvalue=myvalue+15
    if chess[i][j + 1] == chess[i][j + 2] == chess[i][j + 3] == chess[i][j + 4] == 1:
        enevalue=enevalue+12
    if chess[i][j + 1] == chess[i][j + 2] == chess[i][j + 3] == chess[i][j + 4] == 2:
        myvalue=myvalue+15
    if chess[i + 1][j + 1] == chess[i + 2][j + 2] == chess[i + 3][j + 3] == chess[i + 4][j + 4] == 1:
        enevalue=enevalue+12
    if chess[i + 1][j + 1] == chess[i + 2][j + 2] == chess[i + 3][j + 3] == chess[i + 4][j + 4] == 2:
        myvalue=myvalue+15

    if chess[i - 1][j - 1] == chess[i - 2][j - 2] == chess[i - 3][j - 3] == chess[i - 4][j - 4] == 1:
        enevalue = enevalue + 12
    if chess[i - 1][j - 1] == chess[i - 2][j - 2] == chess[i - 3][j - 3] == chess[i - 4][j - 4] == 2:
        myvalue = myvalue + 15
    if chess[i + 1][j - 1] == chess[i + 2][j - 2] == chess[i + 3][j - 3] == chess[i + 4][j - 4] == 1:
        enevalue=enevalue+12
    if chess[i + 1][j - 1] == chess[i + 2][j - 2] == chess[i + 3][j - 3] == chess[i + 4][j - 4] == 2:
        myvalue=myvalue+15
    if chess[i - 1][j + 1] == chess[i - 2][j + 2] == chess[i - 3][j + 3] == chess[i - 4][j + 4] == 1:
        enevalue = enevalue + 12
    if chess[i - 1][j + 1] == chess[i - 2][j + 2] == chess[i - 3][j + 3] == chess[i - 4][j + 4] == 2:
        myvalue = myvalue + 15


    totalvalue=myvalue+enevalue
    return totalvalue


def isWin(chess):
    for i in range(1,11):
        for j in range(1,11):
            if chess[i][j]==chess[i+1][j]==chess[i+2][j]==chess[i+3][j]==chess[i+4][j]==1:
                return 0
            if chess[i][j] == chess[i + 1][j] == chess[i + 2][j] == chess[i + 3][j] == chess[i + 4][j] == 2:
                return 1
            if chess[i][j]==chess[i][j+1]==chess[i][j+2]==chess[i][j+3]==chess[i][j+4]==1:
                return 0
            if chess[i][j] == chess[i][j + 1] == chess[i][j + 2] == chess[i][j + 3] == chess[i][j + 4] == 2:
                return 1
            if chess[i][j]==chess[i+1][j+1]==chess[i+2][j+2]==chess[i+3][j+3]==chess[i+4][j+4]==1:
                return 0
            if chess[i][j] == chess[i + 1][j + 1] == chess[i + 2][j + 2] == chess[i + 3][j + 3] == chess[i+4][j+4] == 2:
                return 1
            if j>4:
                if chess[i][j] == chess[i + 1][j-1] == chess[i + 2][j-2] == chess[i + 3][j-3] == chess[i + 4][j-4] == 1:
                    return 0
                if chess[i][j] == chess[i + 1][j-1] == chess[i + 2][j-2] == chess[i + 3][j-3] == chess[i + 4][j-4] == 2:
                    return 1

def main():
    #t.Turtle().screen.delay(0)
    initBoard()
    chess=initChess()
    #t.done()
    while(True):
        while(True):
            try:
                x, y = map(int, input("你的回合:").split())
            except:
                print('格式错误!请输入正确坐标')
                continue
            if x<1 or x>10 or y<1 or y>10:
                print('超出边界!')
            elif chess[x][y]!=0:
                print('该位置已有棋子!')
            else:
                break
        chess[x][y]=1
        blackchess(x,y)
        #drawChess(chess)
        if(isWin(chess)==0):
            print('you win!')
            break
        m,n=AI(chess)
        chess[m][n]=2
        #drawChess(chess)
        whitechess(m,n)
        if(isWin(chess)==1):
            print('you lose!')
            break

    t.done()

main()
