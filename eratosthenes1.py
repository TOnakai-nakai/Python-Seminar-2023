from math import sqrt

def eratosthenes(n):
    list = range(3, n+1, 2)
    prime = [2]
    i = 3
    while(i <= sqrt(n)):
        prime += [i]
        list = [j for j in list if j % i != 0] # 毎回リストをつくっているので，非効率
        i = list[0]
    prime += list
    return prime

print(eratosthenes(1000))