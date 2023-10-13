from typing import List, Union, Any

N = int(input())
P = list(map(int, input().split()))

P.sort()
T: list[Union[int, Any]] = list()
for i in range(len(P)):
    if len(T):
        T.append(T[-1] + P[i])
    else:
        T.append(P[i])
total = 0
for i in range(len(T)):
    total = total + T[i]
print(total)


