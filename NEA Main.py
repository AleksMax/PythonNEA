import csv
import random

authList = [] 
p1Total = 0
p2Total = 0
roundNo = 1

def main():
    global p1Total
    global p2Total
    global roundNo
    
    readFile()
    player1 = login()
    player2 = login()
    
    while player1 == player2:
        print("You cannot play as the same person twice!")
        player2 = login()
    for i in range(5):
        p1Total += roll(player1,roundNo)
        p2Total += roll(player2,roundNo)
        roundNo += 1

    winList = winner(p1Total,p2Total,player1,player2)

    write(winList)
    sort()
    return

def readFile():
    f = open("auth.csv", "r")
    file = csv.reader(f)
    for row in file:
        authList.append(row)
    return

def login():
    done = False
    while not done:
        userName = input("Input your username: ")
        passWord = input("Input your password: ")
        x = 0
        for i in authList:
            if userName == authList[x][0] and passWord == authList[x][1]:
                print("Welcome!")
                done = True
                break
            x +=1
        if done != True:
            print("Access Denied")
    return userName

def roll(player,roundNo):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rTotal = dice1 + dice2
    check = rTotal % 2

    print("\n---=== Round "+str(roundNo)+" ===---")
    print(player+"'s go")
    print("\n\nRoll 1:",dice1)
    print("Roll 2:",dice2)

    if check == 0:
        print("\nYour score was even, we added 10 points!")
        rTotal += 10
    if check != 0:
        print("\nYour score was odd, we took 5 points!")
        rTotal -= 5
    if dice1 == dice2:
        dice3 = random.randint(1,6)
        rTotal += dice3
        print("\nAnd ... you rolled a double!")
        print("Therefore, you get to roll a third dice!")
        print("Lucky Roll:",dice3)
    if rTotal < 0:
        rTotal = 0

    print("\nYour Total was: ", rTotal)
    
    input("\nPress Enter to Continue: \n")
    return rTotal

def winner(p1Total,p2Total,player1,player2):
    if p1Total == p2Total:
        print("You Drew!")
        print("Time for the Golden Roll!")
        while p1Total == p2Total:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            p1Total += dice1
            p2Total += dice2
        
    if p1Total > p2Total:
        print("\n---------------------\n")
        print("Player "+player1+" won!")
        print("Total Score:",p1Total)
        winList = [p1Total,player1]
    if p2Total > p1Total:
        print("\n---------------------\n")
        print("Player "+player2+" won!")
        print("Total Score:",p2Total)
        winList = [p2Total,player2]
    return winList

def write(winList):
    f = open("scores.csv", "a",newline="")
    file = csv.writer(f)
    file.writerow(winList)
    return

def sort():
    sortList = []
    f = open("scores.csv", "r")
    file = csv.reader(f)
    for i in file:
        sortList.append(i)
    x=0
    for i in sortList:
        sortList[x][0] = int(sortList[x][0])
        x+=1
    sortList.sort(reverse=True)
    y=0
    for i in range(5):
        print("\nName: ",sortList[y][1])
        print("Score: ",sortList[y][0])
        y+=1
    
main()
