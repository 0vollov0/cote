N, K = map(int, input().split())
A = list()
for _ in range(N):
    A.append((int(input())))

# N = 10
# K = 4200
# A = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

# N = 10
# K = 4790
# A = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

total = 0
while K > 0:
    coin = A.pop()
    if coin <= K:
        cnt = K // coin
        K = K - (coin * cnt)
        total = total + cnt
print(total)
