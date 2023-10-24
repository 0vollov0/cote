N = int(input())

A = N // 5
AR = N % 5
while A > 0 and (AR % 3) != 0:
    A = A - 1
    AR = AR + 5

if AR % 3 > 0:
    print(-1)
else:
    print(A + AR // 3)
