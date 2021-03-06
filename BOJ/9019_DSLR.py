##BFS에서 역추적할 때는 전체의 과정을 기록하면 안되고(depth를 알 수 없음, 마지막 한단계만 구해서 역추적해야함)
import collections
import sys

sys.setrecursionlimit(1000000000)
T = int(input())
how = ['']*10000
From = [0]*10000
def D(num):
    return ((num*2)%10000, "D")
def S(num):
    return (num-1 if num>1  else 9999, "S")
def L(num):
    rem = num//1000
    return ((num%1000)*10+rem, "L")
def R(num):
    return ((num%10)*1000+num//10, "R")
def next(num):
    q = collections.deque()
def next(num):
    arr = []
    arr.append(((num * 2) % 10000, "D"))
    arr.append((num - 1 if num > 0 else 9999, "S"))
    first = num // 1000
    arr.append(((num % 1000)*10 + first, "L"))
    last = num % 10
    arr.append((last * 1000 + num // 1000, "R"))
    return arr


for _ in range(T):
    From = [-1 for _ in range(10000)]
    How = ["" for _ in range(10000)]
    Dist = [-1 for _ in range(10000)]
    a, b = map(int, input().split())
    queue = collections.deque()
    queue.append(a)
    Dist[a] = 0
    From[a] = -1
    How[a] = ""
    while queue:
        curr = queue.popleft()
        for num, how in map(lambda x:[D(x), S(x), L(x), R(x)], curr):
            if Dist[num] == -1:
                From[num] = curr
                Dist[num] = Dist[curr] + 1
                How[num] = how

    ans = ""
    while b != a:
        ans += How[b]
        b = From[b]
    print(ans[::-1])
