def print19(s, e):
    for i in range(s, e+1):
        print(i, end=" ")
    print()
    


s = int(input("시작 값 입력: "))
e = int(input("끝 값 입력: "))


if s < e :
    print19(s, e)
else :
    print("시작 값이 끝 값보다 작아야 합니다.")
