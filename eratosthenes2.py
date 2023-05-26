def eratosthenes(n):
    list = [False] + [True]*(n-1)
    prime = []

    for i in range(2, n+1):
        if list[i-1]:   #リストのi番目がTrueだったら
            prime += [i] #iを素数のリストに追加 
            if i <= n**0.5:
                for j in range(i, n+1, i):
                    list[j-1] = False
    return prime

print(eratosthenes(1000))