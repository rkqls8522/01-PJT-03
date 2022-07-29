import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())
c = 0
for i in range(t):
    i = int(input()) #필요없는 줄
    j = list(input().split(' '))
    intList = list(map(int,j))
    sum = 0
    c += 1

    # 평균값 구하기
    for z in intList:
        sum += z
    avr = round(sum/len(intList),0)

    #평균보다 낮은 값 갯수 세기
    count = 0
    for z in intList:
        if z <= avr:
            count += 1

    print(f'#{c} {count}')