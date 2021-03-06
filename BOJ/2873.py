import sys

input = sys.stdin.readline
print= sys.stdout.write
n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
s = ""
if n % 2 == 1:
    for i in range(n):
        if i % 2 == 0:
            s += "R" * (m - 1)  # 짝수행에서는 오른쪽으로 끝까지 이동
            if i != (n - 1):
                s += "D"  # 끝부부에서 아래로 한칸 이동
        else:
            s += "L" * (m - 1)  # 홀수행에서는 왼쪽으로 쭉 이동
            s += "D"
elif m % 2 == 1:  # 열이 홀수면
    for j in range(m):
        if j % 2 == 0:
            s += "D" * (n - 1)  # 짝수행에서는 아래로 끝까지 이동
            if j != (m - 1): #끝부분에서는 오른쪽으로 한칸 이동
                s += "R"
        else:
            s += "U" * (n - 1) #홀수행에서는 위로 끝까지이동
            s+= 'R'
else: #둘다 짝수면
    x=0
    y=1 #검정칸(방문하지 않는 칸)의 좌표. 시작칸이 0,0이 흰칸이므로 합이 홀수면 검정칸
    for i in range(n):
        for j in range(m):
            if (i+j)%2==1: #검정칸이면서
                if a[x][y] > a[i][j]: #칸의 값이 최소가 되는 칸을 찾으면 이 칸이 바로 이동할 수 없는 칸(값이 최대가 되야하므로)
                    x = i
                    y = j
    x1=y1=0 #처음 위치
    x2=n-1
    y2=m-1
    s2=""
    while x2-x1>1: #차이가 2칸 이상이면
        if x1//2 <x//2: #두 칸씩 전진하므로 2개씩 묶어서 나눠주면 됨 ->현재 칸에 이동불가 칸이 없으면 2칸 이동
            s+= 'R'*(m-1)
            s+= "D"
            s+="L"*(m-1)
            s+= "D"
            x1+=2 #행 2칸 증가
        if x//2 <x2//2: #B의 경우 현재칸의 2칸 범위에 이동불가 칸이 없으면 2칸 이동
            s2+="R"*(m-1) #B는 역순으로
            s2+= "D"
            s2+= "L"*(m-1)
            s2+= "D"
            x2-=2
    while y2 - y1 > 1: #차이가 2칸 이상이면
        if y1 // 2 < y // 2: #2칸이내에 이동불가칸이 없으면
            s += 'DRUR'
            y1 += 2
        if y // 2 < y2 // 2:
            s2 += 'DRUR'
            y2 -= 2
    if y == y1: #이동불가 칸이 첫번째면
        s += 'RD'
    else: #이동불가 칸이 두번째면
        s += 'DR'
    s += s2[::-1]
    print(s)
