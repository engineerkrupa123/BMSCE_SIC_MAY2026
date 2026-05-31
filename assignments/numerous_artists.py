def solve():
    
    n = int(input().strip())
    arr = list(map(int, input().split()))
    m = int(input().strip())
    brr = list(map(int, input().split()))
    
    
    freq_brr = {}
    for num in brr:
        freq_brr[num] = freq_brr.get(num, 0) + 1
        
    
    for num in arr:
        if num in freq_brr:
            freq_brr[num] -= 1

   
    missing_numbers = []
    for num, count in freq_brr.items():
        if count > 0:
            missing_numbers.append(num)
            
   
    missing_numbers.sort()
    
    
    print(*(missing_numbers))

if __name__ == '__main__':
    solve()