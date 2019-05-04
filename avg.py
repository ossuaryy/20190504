def avg(a, b, c):
    return (a + b + c)/3

n1 = int(input("첫 번째 정수: "))
n2 = int(input("두 번째 정수: "))
n3 = int(input("세 번째 정수: "))

print(n1, ",", n2, ",", n3, "의 평균은", avg(n1, n2, n3), "입니다.")
