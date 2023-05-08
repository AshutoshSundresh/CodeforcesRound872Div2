t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    seats = list(map(int, input().split()))
    
    right = 0
    left = 0
    p = 0
    
    v = [-1]
    s = set()
    
    for i in range(n):
        x = seats[i]
        
        # Count the number of people choosing seats on the left side
        if x == -2:
            left += 1
        elif x == -1:
            right += 1
        # Count the number of people choosing specific seats and store them in a set
        else:
            p += 1
            s.add(x)
    
    v += sorted(s)
    v.append(-2)
    
    ans = 0
    
    for i in range(len(v)):
        x = v[i]
        
        # Calculate the maximum number of people for the first seat choice
        if i == 0:
            ans = max(ans, min(left + len(v) - 2, m))
        
        # Calculate the maximum number of people for the last seat choice
        elif i == len(v) - 1:
            ans = max(ans, min(right + len(v) - 2, m))
        
        # Calculate the maximum number of people for other seat choices
        else:
            ans = max(ans, 1 + min(right + i - 1, x - 1) + min(left + len(v) - i - 2, m - x))
    
    print(ans)
