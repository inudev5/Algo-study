# #최대값을 구하는 문제이기 때문에 N개의 알파벳이 주어지면
# #알파벳을 9부터 큰 순서대로 N개 바꾸면됨
# from sys import stdin
# alpha = dict()##문자값과 숫자 변환시켜주는 배열
# def calc(a, letters, d):
#     m = len(letters)
#     sum = 0
#     for i in range(m):
#         alpha[letters[i]] = d[i]
#     for word in a:
#         now = 0
#         for char in word:
#             now = now*10+ alpha[char]
#         sum+=now
#     return sum
# def next_permutation(N, A):
#     ans = []
#     i = N - 1
#     while i > 0 and A[i] <= A[i - 1]:  # 내림차순인지 검사한다.
#         i -= 1
#     if i <= 0:
#         return False
#     j = N - 1
#     while A[j] <= A[i - 1]:  # 뒷 숫자들은 이미 내림차순이므로 i-1보다 큰 첫번째 수가 최소값
#         j -= 1
#     A[i - 1], A[j] = A[j], A[i - 1]
#     j = N-1
#     while i<j:
#         A[i], A[j] = A[j], A[i]
#         i+=1
#         j-=1
#     return True
# N = int(input())
# a = ['']*N
# letters = set()#중복제거
# for i in range(N):
#     a[i] = stdin.readline()
#     letters |= set(a[i]) #merge 연산자, letters.update(set(a[i]))와 같음
# letters = list(letters)
# m = len(letters)
# d=[]
# for i in range(m):
#     d.append(9-i)
# d.sort()
# ans = 0
# while True:
#     now = calc(a, letters, d)
#     if ans<now:
#         ans = now
#     if not next_permutation(m, d):
#         break
# print(ans)
#

##문자를 자릿수로 번역
##가장 수가 큰 문자부터 변환
import collections
from collections import defaultdict

n= int(input())
alpha = defaultdict(int)
nums=[]
for _ in range(n):
    word = list(input())
    nums.append(word)
    for i in range(len(word)):
        alpha[word[i]]+= 10**(len(word)-i-1)

sorted_alpha = collections.OrderedDict(sorted(alpha.items(), key=lambda x:-x[1]))
mapping={}
curr=9
for char in sorted_alpha:
    mapping[char] = curr
    curr-=1
    if curr<0:
        break
res=0
for char,count in alpha.items():
    res+=mapping[char]*count

print(res)




