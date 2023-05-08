def solve():
    # Read the values of n and m
    n, m = map(int, input().split())
    s = n * m
    
    # Read the array of values and sort it in ascending order
    v = list(map(int, input().split()))
    v.sort()

    # Store the minimum and maximum values from the sorted array
    mn1 = v[0]
    mn2 = v[1]
    mx1 = v[-1]
    mx2 = v[-2]

    # Calculate the initial value for the maximal possible sum
    al = 0
    al += (max(n, m) - 1) * (min(m, n)) * mx1
    al += (min(n, m) - 1) * mx2
    al -= (s - 1) * mn1

    # Calculate an alternative value for the maximal possible sum
    a2 = 0
    a2 += mx1 * (s - 1)
    a2 -= (max(n, m) - 1) * (min(m, n)) * mn1
    a2 -= (min(n, m) - 1) * mn2

    # Print the maximum of the two possible sums
    print(max(al, a2))

t = int(input())

for i in range(t):
    solve()



