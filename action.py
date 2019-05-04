temper = int(input("온도를 입력하세요: "))
action = int(input("섭씨에서 화씨로 바꾸려면 0을, 화씨에서 섭씨로 바꾸려면 1을 입력하세요:"))

def fc(temper, action):
    if action == 0:
        return temper*9/5 + 3.2

    elif action == 1:
        return (temper-32)*5/9
    else:
        print( "0 또는 1을 입력하세요" )

if action == 0:
    print(temper, "을 화씨로 바꾸면", fc(temper, action), "입니다.")
elif action == 1:
    print(temper, "을 섭씨로 바꾸면", fc(temper, action), "입니다.")
else:
    fc(temper, action)
