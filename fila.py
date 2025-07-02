N = int(input())
AdA = list(map(int,input().split(' ')))
A = 0
AM = AdA[A-1]
CL = 0
A -= 1
N -= 1
for i in range(N):
    A -= 1
    if AM>=AdA[A]:
        CL += 1
    elif AM<AdA[A]:
        AM = AdA[A]
print(CL)