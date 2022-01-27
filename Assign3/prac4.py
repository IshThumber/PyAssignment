n = int(input())

num = map(int, input().split())
num = list(set(num))
num.remove(max(num))

print(max(num))