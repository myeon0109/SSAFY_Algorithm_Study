n, k, m = map(int,input().split())
n_list = list(map(int,input().split()))
n_list.sort(reverse=True)
max_n = n_list[0]
second = n_list[1]
# 그리디 보다는.. 계산식으로 풀어버린 것 같지만..
sum = max_n*((k//(m+1))*m+k%(m+1)) + second*(k//(m+1))
print(sum)
