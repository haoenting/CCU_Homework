from random import choice
from tkinter import Y

class colors:
    ok = '\033[92m' #GREEN
    warning = '\033[93m' #YELLOW
    fail = '\033[91m' #RED
    reset = '\033[0m' #RESET COLOR

alpha = [[None for j in range(1)] for i in range(33)]

f = open("alpha.txt", 'r')
for line in f.readlines(): #讀取檔案
    ans = line.strip()  # 忽略換行
    alpha[len(ans)].append(ans)

def main():
    count, win, lose = 1, 0, 0
    bool = True
    while bool == True:
        print("Do You Want To Play A Game ?", end ='')
        print(colors.fail + " (Y / N) " + colors.reset, end ='')
        x = input(": ")

        if x == 'Y':
            WL = start()
            
            if WL == True:
                win += 1
            else:
                lose += 1

            print("\n遊戲場次 : ", count)
            print("勝利場次 : ", win)
            print("失敗場次 : ", lose)
            print("勝率 : ", win/count*100, "%\n")
                        
            count += 1
        elif x == 'N':
            bool = False
            print("Good Bye!")
        else:
            print("WTF ???")
     
def start(): # 新遊戲
    print("Let's Start !!")
    bool = False
    while bool == False: # 確認輸入合法長度
        num = int(input("請輸入單字長度 : "))
        if num == 26 or num == 30 or num > 31 or num < 1:
            print("沒有此長度的單字\n")
        else:
            bool = True

    fail = int(input("請輸入失敗容許次數 : "))

    return guess(num, fail)


def guess(num,fail): # 開始猜
    End = None
    while End == None:
        End = choice(alpha[num])
    print(End)
    
    collect = [0] * 26

    end = [a for a in End]
    bool = False # 有沒有猜到答案
    while fail > 0:
        Ans = input("請輸入你的答案 : ")
        if Ans in alpha[num]:
            ans = [a for a in Ans]
            if len(ans) != num: # 長度不對
                print("輸入錯誤的長度 !")
            elif ans == end: # 猜對答案
                bool = True
                break
            else: # 比對正確字元
                ary = out(ans, end, num)
                collect = hint(ans, ary, collect, num)
                fail -= 1
        else:
            print("查無此字 !\n")
        
        if fail != 0:
            print("你還剩下",fail,"次機會 !")

    if bool == False:
        print("You Lose ~~")
        print("The anser is ", end = '')
        print(colors.ok + End + colors.reset)
        return False
    else:
        print("The anser is ",end = '')
        print(colors.ok + End + colors.reset)
        print("You Get It !!")
        return True

def out(ans, end, num): # 答案
    run = list()
    run = end
    ary = [0]*num
    for i in range(num): 
        if ans[i] == end[i]: #是否在正確位置
            ary[i] = 1 
            run[i] = '0'

        if ans[i] not in end: #是否不再答案中
            ary[i] = 3           

    for i in range(num):
        if ans[i] != '0': # 是否在答案中
            if ans[i] in run:
                ary[i] = 2
                run[i] = '0'

    for k in range(num): # 印出判斷        
        if ary[k] == 1:
            print(colors.ok + ans[k] + colors.reset, end = '')
        elif ary[k] == 2:
            print(colors.warning + ans[k] + colors.reset, end = '')
        else:
            print(colors.fail + ans[k] + colors.reset, end = '')
    print('')
    return ary

def hint(ans, ary, collect, num):
    for i in range(num):
        value = ord(ans[i]) - 97
        collect[value] = ary[i]
    
    for i in range(26):
        
        word = chr( i + 97 )
        if collect[i] == 0:
            print(word, end ='')
        elif collect[i] == 1:
            print(colors.ok + word + colors.reset, end = '')
        elif collect[i] == 2:
            print(colors.warning + word + colors.reset, end = '')
       
    print("\n")
    return collect

main()

f.close()