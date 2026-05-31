def solve():
    N = int(input().strip())
    harry_coins = list(map(int, input().split()))
    
    
    Q, X = map(int, input().split())
    
    
    monk_bag = []          
    current_worth = 0      
    harry_ptr = 0          
    
    
    for _ in range(Q):
        instruction = input().strip()
        
        if instruction == "Harry":
            # Harry throws his next coin
            coin_value = harry_coins[harry_ptr]
            harry_ptr += 1
            
            # Push onto Monk's stack
            monk_bag.append(coin_value)
            current_worth += coin_value
            
        elif instruction == "Remove":
            # Pop from Monk's stack
            if monk_bag:
                removed_coin = monk_bag.pop()
                current_worth -= removed_coin
        
       
        if current_worth == X:
            print(len(monk_bag))
            return

    
    print(-1)

if __name__ == '__main__':
    solve()