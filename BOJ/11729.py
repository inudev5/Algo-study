n = int(input())

def solve(n,x,y):
    if n==0:
        return
    solve(n-1, x, 6-x-y) #1,2,3번 중 나머지 칸으로 이동하는 것을 6-x-y로 표현
    print(x, y)
    solve(n-1, 6-x-y, y)
print(2**n-1)
solve(n,1,3)

# D[1] = 1
# D[n] = 2* D[n-1]+1
# D[n]+1 = 2*D[n-1]+2
# D[n]+1 = E[n], E[n] = 2*E[n-1], E[1] = 2 따라서 E[n] = 2**n, D[n] = 2**n-1
# solve(6,1,3) => solve(5,1,2)=> 6번원판 1->3=> solve(5,2,3)

#다이나믹 프로그래밍
# D[1] = 1
# D[n] = 2*D[n-1]+1
# D[n]+1 = 2*(D[n-1]+1)
# E[1] = 2 이면
# E[n] = 2*E[n-1] 일반항
# 따라서 일반항으로 E[n] = 2^n
# 따라서 D[n] = 2^n-1