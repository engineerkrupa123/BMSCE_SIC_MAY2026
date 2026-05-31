def solve():
    n = int(input().strip())
    oranges = list(map(int, input().split()))
    
    
    pivot = oranges[n - 1]
    
    
    k = 0
    for i in range(n - 1):  # Loop through 0 to n-2
        if oranges[i] <= pivot:
            
            oranges[i], oranges[k] = oranges[k], oranges[i]
            k += 1
            
    oranges[k], oranges[n - 1] = oranges[n - 1], oranges[k]
    
    print(*(oranges))

if __name__ == '__main__':
    solve()