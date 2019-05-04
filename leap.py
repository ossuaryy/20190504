def leapCommon(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print("윤년(leap year)입니다.")

    else:
        print("평년(common year)입니다.")


year = int(input("연도  입력: "))
leapCommon(year)
