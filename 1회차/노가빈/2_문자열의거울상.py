import sys

sys.stdin = open("_문자열의거울상.txt")

strList = ['b','d','p','q']
reList = ['d','b','q','p']

t = int(input())
for i in range(t):

    #문자열 거꾸로 하기
    str = input()
    str = "".join(reversed(str))
    str = list(str)
    resultStr = []
    for i in range(len(str)):
        indexNum = strList.index(str[i]) # 새로운 indexNum변수에 입력받은 알파벳의 위치를 기억시킨다
        resultStr.append(reList[indexNum]) # 알파벳을 넣는다
        resultStr = ''.join(resultStr)

# print(resultStr)