import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())
for i in range(t):
    numList = list(map(int,input().split(' ')))
    sum1 = 0
    sum2 = 0

    #짝수 자리 수는 그냥 더하기
    for j in range(len(numList)):
        if j % 2 != 0:
            sum1 += numList[j]
        else:
            sum2 += numList[j]*2 # 홀수 자리 수는 2를 곱해서 더하기

    #result값 구하기 (N의 값 구하기)
    result = 10-((sum1+sum2)%10)
    if result == 10:
        result = 0


    print(f'#{i+1} {result}')

