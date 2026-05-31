def solve():
    
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
       
        b = list(map(int, input().split()))
        b.sort()
        
        g = list(map(int, input().split()))
        g.sort()
        
        
        pattern_boy_first = []
        for i in range(n):
            pattern_boy_first.append(b[i])
            pattern_boy_first.append(g[i])
            
       
        pattern_girl_first = []
        for i in range(n):
            pattern_girl_first.append(g[i])
            pattern_girl_first.append(b[i])
            
        
        is_boy_first_valid = all(pattern_boy_first[i] <= pattern_boy_first[i + 1] for i in range(2 * n - 1))
        is_girl_first_valid = all(pattern_girl_first[i] <= pattern_girl_first[i + 1] for i in range(2 * n - 1))
        
        if is_boy_first_valid or is_girl_first_valid:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()