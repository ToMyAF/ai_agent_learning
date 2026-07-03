import random

# 练习1 数字游戏 练习While循环
def guessing_name():
    number = random.randint(10,30)
    while True:
        user_input = input("你猜现在是数字几？他在10~30以内")
        print(f"你输入的是：{user_input}")
        # 健壮性处理：防止输入非数字导致崩溃
        if not user_input.isdigit():
            print("请输入有效的数字")
            continue;
        
        user_answer = int(user_input)

        if user_answer == number:
            print("恭喜答对了！")
            break
        elif user_answer < number:
            print("太小了")
        else:
            print("太大了")

def gussing_name_2():
    number = random.randint(10,30);
    while  user_input := input("输入你的数字？"):
        print(f"你的数字：{user_input}")
       
def gussing_name_while_3():
    number = random.randint(10,30)
    i = 0
    while True:
        user_input = input("输入你的数字？")
        if not user_input.isdigit():
            print("不是合法数字哟")
            continue;
        
        i +=1 # python 没有++

        if int(user_input) == number:
            print("恭喜答对!")
            break
        if i == 3:
            print("抱歉，你尝试了3次都没有成功，程序主动退出！")
            break
        
        print(f"猜错了，还剩{3-i}次机会")

def gussing_name_for_4():
    number = random.randint(10,30)
    for i in range(3):
        user_answer = int(input(f"请输入你的数字，这是第{i+1}次机会，总共3次机会"))
        if user_answer == number:
            print("Bingo 恭喜")
            break
        else:
            print("别灰心，你还能再次尝试！")

def gussing_game_for_5():
    number = random.randint(10,30)
    for i in range(3):
        user_answer = int(input(f"请输入你的数字"))
        if user_answer == number:
            print("Bingo 恭喜")
            return
        print(f"猜错了，还剩{2-i}次机会")
    print("抱歉，3次都没有成功，程序主动退出了~")

if __name__ == "__main__":
    # guessing_name()
    # gussing_name_2()
    # gussing_name_while_3()
    # gussing_name_for_4()
    gussing_game_for_5()