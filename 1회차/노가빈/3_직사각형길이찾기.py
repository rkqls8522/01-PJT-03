import sys

sys.stdin = open("_직사각형길이찾기.txt")
t = int(input())

for i in range(t):
    a, b, c = map(int, input().split(' '))
    numList = [a,b,c]
    num_count = {}

    for num in numList:
        num_count[num] = 0 # 특정 문자 딕셔너리에 추가
    for num in numList:
        num_count[num] = num_count[num] + 1 # 추가한 딕셔너리에서 갯수 더하기
    if len(num_count) <= 2 :
        result = min(num_count.values())
        result = [i for i, j in num_count.items() if j == result]
        print(f'#{i+1} {result[0]}')
    else : 
        print('다시 입력해주세요')
    