N = int(input())
numbers = list(map(int, input().split()))

nums = sorted(list(set(numbers)))
dic = {}
for cnt, i in enumerate(nums):
    dic[i] = cnt

for i in numbers:
    print(dic[i])