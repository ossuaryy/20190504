def leapCommon(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    
    else:
        return False


year = int(input("연도  입력: "))
if leapCommon(year) :
    print("윤년입니다.")
else :
    print("평년입니다.")
