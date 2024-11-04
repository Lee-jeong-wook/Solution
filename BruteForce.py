# 1.
#백준 1868
#100만보다 작고  2 이상의 약수를 가지고 있다면 올바르지 않은 비번
# TC = int(input())
# for _ in range(TC):
#   number = int(input());
#   for i in range(2, 1_000_001):
#     if(number % i == 0): 
#       print("NO")#약수 존재
#       break
#     if i == 1_000_000:
#       print("yes")
# 2.
# 친구 ABC에게 사탕을 나누어 주려고 합니다
# 조건은 아래와 같습니다
"""
1. 남는 사람이 없어야 합니다.
2. A는 B보다 2개 이상 많은 사탕을 가져야 합합니다
3. 셋 중 사탕을 하나도 못 받는 친구는 없어야 합니다.
4. C가 받는 사탕의 수는 짝수입니다
"""
# answer = 0;
# candy = int(input())
# for A in range(0, candy + 1):
#     for B in range(0, candy + 1):
#         for C in range(0, candy + 1):
#             if A + B + C ==  candy:
#                 if(A >= B + 2):
#                     if(A != 0 and B != 0 and C != 0):
#                         if(C % 2 == 0):
#                             answer+=1
# print(answer)