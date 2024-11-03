def rec(n, output):
    if n == M:
        print(output)
        return
    for i in range(1, N + 1):
        rec(n + 1,  output+str(i)+ " ")
    
N, M = map(int, input().split())
rec(0, "")